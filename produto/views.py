from rest_framework import viewsets,permissions
from django_filters.rest_framework import DjangoFilterBackend
from produto.serializers import ProdutoSerializer
from produto.models import Produto


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['setor_fk']
    
    def perform_destroy(self, instance):
        instance.status = False
        instance.save()

    def get_permissions(self):
        if self.action is not 'list':
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]

    def get_queryset(self):
        return super().get_queryset().filter(status=True)