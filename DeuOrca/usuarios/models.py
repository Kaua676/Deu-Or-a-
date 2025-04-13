# usuarios/models.py

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, nome, cpf_cnpj, tipo_usuario, password=None):
        if not email:
            raise ValueError("Usuário precisa de um e-mail")
        email = self.normalize_email(email)
        user = self.model(email=email, nome=nome, cpf_cnpj=cpf_cnpj, tipo_usuario=tipo_usuario)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, cpf_cnpj, tipo_usuario='administrador', password=None):
        user = self.create_user(email, nome, cpf_cnpj, tipo_usuario, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    TIPO_USUARIO = (
        ('administrador', 'Administrador'),
        ('cliente', 'Cliente')
    )

    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=100)
    cpf_cnpj = models.CharField(max_length=20)
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO)
    foto_logo = models.ImageField(upload_to='fotos/', null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'cpf_cnpj', 'tipo_usuario']

    def __str__(self):
        return self.email
