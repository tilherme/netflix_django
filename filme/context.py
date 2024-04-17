from .models import *

def list_recent_movie(request):
    list_film = Film.objects.all().order_by('-creation_date')[0:8] # order decrescente
    return {'list_recent_movie': list_film}

def list_trending_movie(request):
    list_film = Film.objects.all().order_by('-preview')[0:8] # order decrescente
    return {'list_trending_movie': list_film}