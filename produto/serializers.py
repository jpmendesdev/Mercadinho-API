from rest_framework import serializers
from produto.models import Produto
from setor.serializers import SetorSerializer

class ProdutoSerializer(serializers.ModelSerializer):
    setor_detalhes = SetorSerializer(source='setor_fk', read_only=True)
    class Meta:
        model = Produto
        fields = '__all__'

    def validate_quantidade(self, value):
        if value < 10:
            raise serializers.ValidationError("O número de produtos disponíveis não pode ser menor que 10!")
        return value
    
    def validate(self, data):
        if data['preco_de_custo'] > data['preco_de_venda']:
            raise serializers.ValidationError("O preço de custo não pode ser maior que o preço de venda!")
        elif data['quantidade'] > data['setor_fk'].max_produtos:
            raise serializers.ValidationError("A quantidade de produtos não pode exceder a capacidade do setor!")
        return data