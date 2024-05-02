from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import *
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
# def homepage(request):
#     return render(request, 'homepage.html')

class Homepage(TemplateView):
    template_name = 'homepage.html'

    def get(self, request, *args, **kwargs):
        if  request.user.is_authenticated:
           return redirect('filme:home_film')
        else:
            return super().get(request, *args, **kwargs) #redireciona o user para a url final

# def home_filmes(request):
#     list_filmes = Film.objects.all()
#     context = {}
#     context['list_filmes'] = list_filmes
#     return render (request, 'home_filmes.html', context)
    
class EditUser( LoginRequiredMixin,TemplateView):
    template_name = 'edit_user.html'


class CreateUser(TemplateView):
    template_name = 'create_user.html'

class HomeFilms(LoginRequiredMixin, ListView):
    template_name = 'home_filmes.html'
    model = Film
    # object_list

class DetailFilm(LoginRequiredMixin, DetailView):
    template_name = 'detail_film.html'
    model = Film
    # object -> 1 item
    
    def get(self, request, *args, **kwargs):
        movie = self.get_object()
        movie.preview += 1
        movie.save()
        request.user.film_previw.add(movie)

        return super().get(request, *args, **kwargs) #redireciona o user para a url final

    def get_context_data(self, **kwargs):
        context = super(DetailFilm, self).get_context_data(**kwargs) 
        film_relations = Film.objects.filter(category= self.get_object().category) # lista python filtro por category self.get_object() meu object 
        context["film_relations"] = film_relations
        return context              


class SearchFilm(LoginRequiredMixin, ListView):
    template_name = 'search_film.html'
    model = Film
    def get_queryset(self):
        search = self.request.GET.get('query')
        if search:
            object_list = self.model.objects.filter(title__icontains= search)
            return object_list
        else:
            return None
        return super().get_queryset()