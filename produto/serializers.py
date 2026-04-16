from rest_framework import serializers
from produto.models import Produto
from setor.serializers import SetorSerializer

class ProdutoSerializer(serializers.ModelSerializer):
    setor = serializers.ReadOnlyField(source='setor_fk.nome')
    class Meta:
        model = Produto
        fields = ['id','nome','tipo','descricao','quantidade','status','setor_fk',
                  'setor','preco_de_custo','preco_de_venda','data_de_cadastro']

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