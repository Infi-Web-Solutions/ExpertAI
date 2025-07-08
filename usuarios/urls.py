from django.urls import path
from .import views
app_name = 'usuarios' 
urlpatterns = [
    path('', views.login_view, name='user_login' ),
    path('register/', views.register_view, name='register' ),    
    path('plataforma', views.plataforma, name='plataforma'),
    path('user_dashboard', views.user_dashboard, name='user_dashboard'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('solicitacoes/delete/<int:id>/', views.delete_solicitacao, name='delete_solicitacao'),
    path('usuarios', views.listar_usuarios, name='listar_usuarios'),
    path('create/users', views.create_users_view, name='criar_usuarios' ),
    path('update-user-status/', views.update_user_status, name='update_user_status'),
    path('update-user-tokens/', views.update_user_tokens, name='update_user_tokens'),
    path('editar/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('editar/tokens/<int:id>/', views.editar_tokens, name='editar_tokens'),    
    path('deletar/<int:id>/', views.deletar_usuario, name='deletar_usuario'),
    path('deletar/tokens/<int:id>/', views.deletar_tokens, name='deletar_tokens'),    
    path('dismiss-tutorial/', views.dismiss_tutorial, name='dismiss-tutorial'),
    path('tokens', views.listar_tokens, name='listar_tokens'),
    
]
