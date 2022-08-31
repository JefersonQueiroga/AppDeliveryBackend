from django.db import models
from usuario.models import User

class Loja(models.Model):
    nome = models.CharField(max_length=150)
    cidade = models.CharField(max_length=150)
    telefone= models.CharField(max_length=150)


class Categoria(models.Model):
    nome = models.CharField(max_length=150)

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    loja = models.ForeignKey(Loja,on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    exclusivo = models.BooleanField(default=False)
    descricao = models.TextField(null=True)
    imagem = models.FileField(null=True)

class Pedido(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=6, decimal_places=2)
    produtos = models.ManyToManyField(Produto)
    loja = models.ForeignKey(Loja,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)




