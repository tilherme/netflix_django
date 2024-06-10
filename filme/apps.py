from django.apps import AppConfig
from django.db.models.signals import post_migrate
import os

class FilmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filme'

    def ready(self):
        # Conectar ao sinal post_migrate para executar a função após as migrações
        post_migrate.connect(self.create_admin_user, sender=self)

    def create_admin_user(self, **kwargs):
        from .models import User  # Importar o modelo aqui para evitar problemas de importação precoce
        email = os.getenv('EMAIL_ADMIN')
        password = os.getenv('SENHA_ADMIN')
        
        if email and password:  # Certifique-se de que os valores não são None
            user = User.objects.filter(email=email).first()

            if not user:
                usuario = User.objects.create_superuser(username='admin', email=email, password=password,
                                                        is_active=True, is_staff=True)
                print(f"Superuser {usuario.username} created")
            else:
                usuario = user
                print(f"Superuser with email {email} already exists")
        else:
            print("Admin email or password not provided in environment variables")
