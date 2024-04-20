from django.urls import path, include
from .views import *

app_name = 'filme'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', HomeFilms.as_view(), name='home_film'),
    path('filmes/<int:pk>', DetailFilm.as_view(),name='detail_film'),
    path('pesquisa/', SearchFilm.as_view(), name='pesquisa')
]
