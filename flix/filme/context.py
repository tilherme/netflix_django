from .models import *

def list_recent_movie(request):
    list_film = Film.objects.all().order_by('-creation_date')[0:8] # order decrescente
    if list_film:
        movie_destaque = list_film[0]
    else: 
        movie_destaque =  None
    return {'list_recent_movie': list_film, 'movie_destaque': movie_destaque}

def list_trending_movie(request):
    list_film = Film.objects.all().order_by('-preview')[0:8] # order decrescente
    return {'list_trending_movie': list_film}

