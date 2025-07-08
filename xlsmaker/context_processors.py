def tokens_disponiveis(request):
    if request.user.is_authenticated:
        return {'tokens_disponiveis': request.session.get('tokens_disponiveis', 0)}
    return {'tokens_disponiveis': 0}