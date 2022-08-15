from cgitb import lookup
from rest_framework import generics
from pedido.models import Loja, Pedido, Produto, Categoria
from .serializers import * 

class ProdutoCreateViewSet(generics.CreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class PedidoCreateViewSet(generics.CreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class CategoriaCreateViewSet(generics.CreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class LojaListViewSet(generics.ListAPIView):
    serializer_class = LojaSerializer
    queryset = Loja.objects.all()


class ProdutoListViewSet(generics.ListAPIView):
    serializer_class = ProdutoSerializer
    queryset = Produto.objects.all()

class PedidoListViewSet(generics.ListAPIView):
    serializer_class = PedidoSerializer
    
    def get_queryset(self):
        loja = Loja.objects.get(pk=self.kwargs['id'])

        queryset = Pedido.objects.filter(loja = loja)
        return queryset

class ProdutoListDetailViewSet(generics.RetrieveAPIView):
    serializer_class = ProdutoSerializer
    lookup_field = 'id'
    
    def get_queryset(self):
        return Produto.objects.filter(id=self.kwargs['id'])
    
class ProdutoListByCategoryViewSet(generics.ListAPIView):
    serializer_class = ProdutoSerializer

    def get_queryset(self):
        category = Categoria.objects.get(pk=self.kwargs['category_id'])
        queryset = Produto.objects.filter(categoria = category)
        return queryset
