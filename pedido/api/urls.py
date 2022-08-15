from django.urls import path
from .viewssets import *

urlpatterns = [
    path("listar_lojas/", LojaListViewSet.as_view(), name="listar_lojas"),
    path("listar_produtos/", ProdutoListViewSet.as_view(), name="listar_produtos"),
    path("listar_pedidos_da_loja/<int:id>/", PedidoListViewSet.as_view(), name="listar_pedidos_da_loja"),
    path("cadastrar_loja/", LojaCreateViewSet.as_view(), name="cadastrar_loja"),

]