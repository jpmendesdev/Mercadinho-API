from rest_framework import serializers
from usuarios.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        # extra_kwargs = {'is_superuser':{'read_only':True},
        #                  'is_staff':{'read_only':True},
        #                  'role':{'read_only':True},}
        
    def create(self, validated_data):
        user = self.context['request'].user
        role_pretendida = validated_data.get('role')
        if role_pretendida == 'ADM' and user.is_superuser:
            validated_data['role'] = 'ADMIN'
            validated_data['is_staff'] = True
        else:
            validated_data['role'] = 'LOJA'
            validated_data['is_staff'] = False
            validated_data['is_superuser'] = False

        return Usuario.objects.create_user(**validated_data)