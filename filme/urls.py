from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Homepage.as_view()),
    path('filmes/', HomeFilms.as_view())

]