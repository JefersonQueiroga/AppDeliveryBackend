from django.urls import path
from .viewssets import *

urlpatterns = [
    path("listar_lojas/", LojaListViewSet.as_view(), name="listar_lojas"),
    path("listar_produtos/", ProdutoListViewSet.as_view(), name="listar_produtos"),
    path("listar_pedidos_da_loja/<int:id>/", PedidoListViewSet.as_view(), name="listar_pedidos_da_loja"),
<<<<<<< HEAD
    path("cadastrar_loja/", LojaCreateViewSet.as_view(), name="cadastrar_loja"),
    path("cadastrar_produto/", ProdutoCreateViewSet.as_view(), name="criar_produto"),
    path("cadastrar_pedido/", PedidoCreateViewSet.as_view(), name="criar_pedido"),
=======
    path("listar_detalhes_produto/<int:id>/", ProdutoListDetailViewSet.as_view(), name="listar_detalhes_produto"),
    path("listar_produtos_pela_categoria/<int:category_id>/", ProdutoListByCategoryViewSet.as_view(), name="listar_produtos_pela_categoria"),

>>>>>>> eb3496230f90c0505709e63d8d5f453fb7b557fc
]