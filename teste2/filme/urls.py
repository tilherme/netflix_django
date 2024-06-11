from django.urls import path, reverse_lazy
from .views import *
from django.contrib.auth import views as auth_view
app_name = 'filme'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', HomeFilms.as_view(), name='home_film'),
    path('filmes/<int:pk>', DetailFilm.as_view(),name='detail_film'),
    path('pesquisa/', SearchFilm.as_view(), name='pesquisa'),
    path('login/', auth_view.LoginView.as_view(template_name = 'login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name ='logout.html'), name='logout'),
    path('change_password/', auth_view.PasswordChangeView.as_view(template_name='edit_user.html', 
                                                                      success_url=reverse_lazy('filme:home_film')), name='change_password'),
    path('update/<int:pk>', EditUser.as_view(), name='update'),
    path('create_user/', CreateUser.as_view(), name='create_user'),
    
]
