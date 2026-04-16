from rest_framework import serializers
from usuarios.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        extra_kwargs = {'is_superuser':{'read_only':True},
                        'is_staff':{'read_only':True},
                        'role':{'read_only':True},}
