from django.urls import path
from .viewssets import *

urlpatterns = [
    path("listar_lojas/", LojaListViewSet.as_view(), name="listar_lojas"),
    path("listar_produtos/", ProdutoListViewSet.as_view(), name="listar_produtos"),
    path("listar_pedidos_da_loja/<int:id>/", PedidoListViewSet.as_view(), name="listar_pedidos_da_loja"),
    path("cadastrar_loja/", LojaCreateViewSet.as_view(), name="cadastrar_loja"),
    path("cadastrar_produto/", ProdutoCreateViewSet.as_view(), name="criar_produto"),
    path("cadastrar_pedido/", PedidoCreateViewSet.as_view(), name="criar_pedido"),

]