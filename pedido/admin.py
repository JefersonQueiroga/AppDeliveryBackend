from django.contrib import admin
from pedido.models import *
# Register your models here.

admin.site.register(Loja)
admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Pedido)