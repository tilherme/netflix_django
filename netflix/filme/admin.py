from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

campos = list(UserAdmin.fieldsets)
campos.append(
    ("vistos", {'fields':('film_previw',)})
)
UserAdmin.fieldsets = tuple(campos)


admin.site.register(Film)
admin.site.register(Episod)
admin.site.register(User, UserAdmin)