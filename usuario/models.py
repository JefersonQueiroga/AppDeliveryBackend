from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from rest_framework_simplejwt.tokens import RefreshToken

class UserManager(BaseUserManager):

    def create_user(self, username,email,password=None,phone=''):
        if username is None:
            raise TypeError('Usuário deve informar o nome')
        if email is None:
            raise TypeError('Users deve informar o Email')
    
        user = self.model(username=username,email=self.normalize_email(email),phone=phone)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user 

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, db_index=True, unique=True)
    phone =  models.CharField(max_length=50, db_index=True,null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
    def get_token_access(self):
        refresh = RefreshToken.for_user(self)
        return str(refresh.access_token)


class Endereco(models.Model):
    cep = models.CharField(max_length=10)
    estado = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    rua = models.CharField(max_length=255)
    numero = models.IntegerField()
    complemento = models.TextField(null=True)
    bairro = models.CharField(max_length=255)
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    TIPO_CHOICES = (
        ("Casa","Casa"),
        ("Trabalho", "Trabalho"),
    )
    tipo = models.CharField(max_length=255, choices=TIPO_CHOICES)