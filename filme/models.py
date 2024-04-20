from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

LIST_CATEGORY = (
    ("ACAO", "Ação"),
    ("TERROR", "Terror"),
    ("COMEDIA", "Comedia"),
    ("Outros", "Outros"),


)# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb')
    category = models.CharField(max_length=100, choices=LIST_CATEGORY) 
    description =  models.TextField(max_length=100)
    preview = models.IntegerField(default =0)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    

class Episod(models.Model):
    film = models.ForeignKey('Film', related_name='episodios', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    link = models.URLField()
    
    def __str__(self):
        return self.title

class User(AbstractUser):
    film_previw = models.ManyToManyField('Film')