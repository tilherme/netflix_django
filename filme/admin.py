from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
admin.site.register(Film)
# Register your models here.
admin.site.register(Episod)
admin.site.register(User, UserAdmin)