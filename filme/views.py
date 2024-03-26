from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.
# def homepage(request):
#     return render(request, 'homepage.html')

class Homepage(TemplateView):
    template_name = 'homepage.html'

# def home_filmes(request):
#     list_filmes = Film.objects.all()
#     context = {}
#     context['list_filmes'] = list_filmes
#     return render (request, 'home_filmes.html', context)
    
class HomeFilms(ListView):
    template_name = 'home_filmes.html'
    model = Film
    # object_list

class DetailFilm(DetailView):
    template_name = 'detail_film.html'
    model = Film
