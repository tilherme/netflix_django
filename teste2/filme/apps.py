from django.apps import AppConfig

class FilmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filme'

    def ready(self):
        from .models import User 
        import os

        email = os.getenv('EMAIL_ADMIN')
        password = os.getenv('SENHA_ADMIN')
        
        user = User.objects.filter(email=email)

        if not user:
            User.objects.create_superuser(username='admin', email=email, password=password,
                                                        is_active=True, is_staff=True)
