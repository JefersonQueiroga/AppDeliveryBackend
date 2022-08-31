from rest_framework import serializers
from pedido.models import Pedido, Loja, Produto,Categoria

class LojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = ('__all__')

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ('__all__')

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('__all__')

class ProdutoSerializer(serializers.ModelSerializer):
    loja = LojaSerializer()
    categoria = CategoriaSerializer()
    class Meta:
        model = Produto
        fields = ('__all__')
class ProdutoDetalheSerializer(serializers.ModelSerializer):
    loja = LojaSerializer()
    categoria = CategoriaSerializer()
    class Meta:
        model = Produto
        fields = ('__all__')