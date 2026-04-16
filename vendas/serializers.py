from rest_framework import serializers
from vendas.models import Venda

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = '__all__'
        extra_kwargs = {
            'qtd_de_produtos':{'required':False}
        }

    def create(self, validated_data):
        produtos = validated_data.pop('produtos',[])
        validated_data['qtd_de_produtos'] = len(produtos)
        instancia = Venda.objects.create(**validated_data)
        instancia.produtos.set(produtos)
        valor_total = 0
        for produto in produtos:
            valor_total += produto.preco_de_venda
        instancia.valor_total = valor_total
        instancia.save()
        return instancia