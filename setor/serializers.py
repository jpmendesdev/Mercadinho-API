from rest_framework import serializers
from .models import Setor

class SetorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setor
        fields = '__all__'

    def validate_max_produtos(self,value):
        if value < 10:
            raise serializers.ValidationError("A quantidade máxima de produtos por setor não pode ser menor que 10!")
        return value