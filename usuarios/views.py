from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from xlsmaker.models import Solicitacao 
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from xlsmaker.models import UserProfile 
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.db.models import Q


# Função auxiliar para verificar se é admin
def is_admin(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)

def register_view(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirma_password = request.POST.get('confirma_password')

        if password != confirma_password:
            messages.error(request, 'As senhas não coincidem!')
            return render(request, 'register.html', {'username': username, 'email': email})
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Nome de usuário já está em uso!')
            return render(request, 'register.html', {'email': email})
        
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.is_active = False
            user.save()
            messages.success(request, 'Cadastro realizado com sucesso! Faça seu login.')
            return redirect('usuarios:user_login')
        except Exception as e:
            messages.error(request, f'Erro ao criar usuário: {str(e)}')
            return render(request, 'register.html')


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username').strip()
        password = request.POST.get('password').strip()
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if not user.is_active:
                messages.error(request, '❌ Sua conta está desativada. Entre em contato com o suporte.')
                return render(request, 'login.html')
            # Resetar tutorial para novos logins
            request.session['show_tutorial'] = True
            request.session['tutorial_dismissed'] = False  
         
            login(request, user)
            if is_admin(user):
                return redirect('usuarios:admin_dashboard')
            else:
                # Criar um perfil automaticamente se ainda não existir
                user_profile, created = UserProfile.objects.get_or_create(user=user, defaults={'tokens_atribuidos': 1000, 'tokens_gastos': 0})         
                return redirect('xlsmaker:dashboard') 
        else:
            messages.error(request, '❌ Erro: email ou senha inválidos!')
            return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('login')

# Painéis de controle
@login_required
def user_dashboard(request):
    context = {'user': request.user}
    return render(request, 'dashboard/user.html', context)

@login_required
@user_passes_test(is_admin, login_url='/auth/login/')
def admin_dashboard(request):    
    query = request.GET.get('q', '')
    solicitacoes_list = Solicitacao.objects.all().order_by('-created_at')
    if query:
        solicitacoes_list = solicitacoes_list.filter(
            Q(nome__icontains=query) | Q(email__icontains=query) | Q(created_at__icontains=query)
        )
    paginator = Paginator(solicitacoes_list, 10)    
    page_number = request.GET.get('page') 
    solicitacoes = paginator.get_page(page_number)     
    context = {'solicitacoes': solicitacoes} 
      # Se for uma requisição AJAX, retorna o HTML parcial
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('dashboard/partials/_users_solicitacoes.html', context)
        return JsonResponse({'html': html})
    return render(request, 'dashboard/admin.html', context)


# @login_required
# @user_passes_test(is_admin, login_url=reverse_lazy('usuarios:user_login'))
# def listar_usuarios(request):
#     usuarios_list = User.objects.all().order_by('-date_joined') 
#     paginator = Paginator(usuarios_list, 10)    
#     page_number = request.GET.get('page')  
#     usuarios = paginator.get_page(page_number) 
#     context = {'usuarios': usuarios}
#     return render(request, 'dashboard/list_users.html', context)

@login_required
@user_passes_test(is_admin, login_url=reverse_lazy('usuarios:user_login'))
def listar_usuarios(request):
    query = request.GET.get('q', '')
    usuarios_list = User.objects.all().order_by('-date_joined')

    if query:
        usuarios_list = usuarios_list.filter(
            Q(username__icontains=query) | Q(email__icontains=query)
        )

    paginator = Paginator(usuarios_list, 10)
    page_number = request.GET.get('page')
    usuarios = paginator.get_page(page_number)

    # Se for uma requisição AJAX, retorna o HTML parcial
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('dashboard/partials/_users_table.html', {'usuarios': usuarios})
        return JsonResponse({'html': html})

    return render(request, 'dashboard/list_users.html', {'usuarios': usuarios})

# @login_required
# @user_passes_test(is_admin, login_url=reverse_lazy('usuarios:user_login'))
# def listar_tokens(request):
#     query = request.GET.get('q', '')
#     user_profile_list = UserProfile.objects.select_related('user').all()
#     if query:
#       user_profile_list = user_profile_list.filter(
#             Q(user__username__icontains=query) | Q(user__email__icontains=query)
#     )
#     for profile in user_profile_list:
#         profile.saldo_tokens = profile.tokens_atribuidos - profile.tokens_gastos
#     paginator = Paginator(user_profile_list, 10)    
#     page_number = request.GET.get('page')  
#     user_profile = paginator.get_page(page_number) 
#     context = {'user_profile': user_profile}
    
#      # Se for uma requisição AJAX, retorna o HTML parcial
#     if request.headers.get('x-requested-with') == 'XMLHttpRequest':
#         html = render_to_string('dashboard/partials/_users_tokens.html', context)
#         return JsonResponse({'html': html})
    
#     return render(request, 'dashboard/list_tokens.html', context)
# @login_required
# @user_passes_test(is_admin, login_url=reverse_lazy('usuarios:user_login'))
# def listar_tokens(request):

#     query = request.GET.get('q', '')
#     user_profile_list = UserProfile.objects.select_related('user').all()

#     if query:
#         user_profile_list = user_profile_list.filter(
#             Q(user__username__icontains=query) |
#             Q(user__email__icontains=query) |
#             Q(tokens_atribuidos__icontains=query)            
#         )

#     # Calcula saldo_tokens dinamicamente
#     for profile in user_profile_list:
#         profile.saldo_tokens = profile.tokens_atribuidos - profile.tokens_gastos

#     paginator = Paginator(user_profile_list, 10)
#     page_number = request.GET.get('page')
#     user_profile = paginator.get_page(page_number)

#     context = {'user_profile': user_profile}

#     if request.headers.get('x-requested-with') == 'XMLHttpRequest':
#         html = render_to_string('dashboard/partials/_users_tokens.html', context)
#         return JsonResponse({'html': html})

#     return render(request, 'dashboard/list_tokens.html', context)

@login_required
@user_passes_test(is_admin, login_url=reverse_lazy('usuarios:user_login'))
def listar_tokens(request):
    query = request.GET.get('q', '')
    user_profile_list = UserProfile.objects.select_related('user').all().order_by('user__username')

    if query:
        # Filtra por texto (username ou email) OU por número exato de tokens
        try:
            query_as_int = int(query)
            user_profile_list = user_profile_list.filter(
                Q(user__username__icontains=query) |
                Q(user__email__icontains=query) |
                Q(tokens_atribuidos=query_as_int)
            )
        except ValueError:
            # Se não for um número, filtra apenas por texto
            user_profile_list = user_profile_list.filter(
                Q(user__username__icontains=query) |
                Q(user__email__icontains=query)
            )

    paginator = Paginator(user_profile_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'user_profile': page_obj,
        'query': query  # Passa a query para manter na paginação
    }

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('dashboard/partials/_user_tokens.html', context)
        return JsonResponse({
            'html': html
        })

    return render(request, 'dashboard/list_tokens.html', context)


@login_required
@user_passes_test(is_admin, login_url=reverse_lazy('usuarios:user_login'))
def create_users_view(request):
    if request.method == 'GET':
        return render(request, 'dashboard/create.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirma_password = request.POST.get('confirma_password')

        if password != confirma_password:
            messages.error(request, 'As senhas não coincidem!')
            return render(request, 'dashboard/create.html', {'username': username, 'email': email})

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Nome de usuário já está em uso!')
            return render(request, 'dashboard/create.html', {'email': email})

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.is_active = False
            user.save()            
            # Criando o perfil do usuário logo após criar o User
            UserProfile.objects.create(user=user)
            messages.success(request, 'Usuário cadastrado com sucesso')
            return redirect('usuarios:listar_usuarios')  # Mantém na mesma página
        except Exception as e:
            messages.error(request, f'Erro ao criar usuário: {str(e)}')
            return render(request, 'dashboard/create.html')



@login_required(login_url="/auth/login/")
def plataforma(request):   
    return HttpResponse('Logado com sucesso na plataforma')


@require_POST
def delete_solicitacao(request, id):
    try:
        solicitacao = Solicitacao.objects.get(id=id)
        solicitacao.delete()
        return JsonResponse({'status': 'success'})
    except Solicitacao.DoesNotExist:
        return JsonResponse({'status': 'error'}, status=404)   



@csrf_exempt  # Apenas se não estiver usando o CSRF token no frontend
def update_user_status(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_id = data.get('user_id')
            is_active = data.get('is_active') == '1'  # Converte para Boolean
            
            user = User.objects.get(id=user_id)
            user.is_active = is_active
            user.save()
            return JsonResponse({'status': 'success', 'is_active': user.is_active})
        except User.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Usuário não encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Método não permitido'}, status=405)


@csrf_exempt  # Apenas se não estiver usando o CSRF token no frontend
def update_user_tokens(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_id = data.get('user_id')
            new_value = data.get('new_value')  # Pegando o valor enviado

            user = UserProfile.objects.get(id=user_id)
            user.tokens_gastos = int(new_value)  # Resetando os tokens gastos
            user.save()

            return JsonResponse({'status': 'success', 'message': 'Tokens resetados com sucesso!'})
        
        except UserProfile.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Usuário não encontrado'}, status=404)
        
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Método não permitido'}, status=405)


def editar_usuario(request, id):
    usuario = get_object_or_404(User, id=id)
    if request.method == 'POST':
        usuario.username = request.POST.get('username')
        usuario.email = request.POST.get('email')
        usuario.is_active = request.POST.get('is_active')
        usuario.save()
        messages.success(request, 'Usuário atualizado com sucesso!')
        return redirect('usuarios:listar_usuarios')

    return render(request, 'dashboard/edit.html', {'usuario': usuario})


def editar_tokens(request, id):
    profile = UserProfile.objects.select_related('user').get(id=id)
    if request.method == 'POST':
        nova_atribuicao = int(request.POST.get('nova_atribuicao', 0))
        tokens_atuais = int(request.POST.get('tokens_actuais', 0))
        profile.tokens_atribuidos = nova_atribuicao + tokens_atuais
        profile.save()
        messages.success(request, 'Tokens atualizados com sucesso!')
        return redirect('usuarios:listar_tokens')
    return render(request, 'dashboard/edit_tokens.html', {'profile': profile})


def deletar_usuario(request, id):
    if request.method == "POST" and request.POST.get("delete"):
        usuario = get_object_or_404(User, id=id)
         # Exclui o perfil se existir
        try:
            usuario.userprofile.delete()
        except UserProfile.DoesNotExist:
            pass  # se o usuário não tiver perfil, ignora
        usuario.delete()
        return JsonResponse({"success": True})    
    return JsonResponse({"error": "Método não permitido"}, status=405)

def deletar_tokens(request, id):
    if request.method == "POST" and request.POST.get("delete"):
        profile = get_object_or_404(UserProfile, id=id)    
        profile.delete()
        return JsonResponse({"success": True})    
    return JsonResponse({"error": "Método não permitido"}, status=405)

def dismiss_tutorial(request):
    if request.method == 'POST':
        # Marcar na sessão que o tutorial foi visto
        if 'dont_show_again' in request.POST:
            request.session['tutorial_dismissed'] = True
        else:
            request.session['tutorial_dismissed'] = False
            request.session['show_tutorial'] = False
            
            
        messages.success(request, 'Configurações de tutorial atualizadas!')
    return redirect('xlsmaker:dashboard')

from django.conf import settings

