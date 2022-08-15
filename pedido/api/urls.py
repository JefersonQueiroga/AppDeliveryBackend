from django.urls import path
from .viewssets import *

urlpatterns = [
    path("listar_lojas/", LojaListViewSet.as_view(), name="listar_lojas"),
    path("listar_produtos/", ProdutoListViewSet.as_view(), name="listar_produtos"),
    path("listar_pedidos_da_loja/<int:id>/", PedidoListViewSet.as_view(), name="listar_pedidos_da_loja"),
    path("listar_detalhes_produto/<int:id>/", ProdutoListDetailViewSet.as_view(), name="listar_detalhes_produto"),
    path("listar_produtos_pela_categoria/<int:category_id>/", ProdutoListByCategoryViewSet.as_view(), name="listar_produtos_pela_categoria"),

]