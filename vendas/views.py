from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from vendas.models import Venda
from vendas.serializers import VendaSerializer


class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.filter(status='ativo')
    serializer_class = VendaSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        instance.status = instance.STATUS['des']
        instance.save()

    def get_queryset(self):
        queryset = Venda.objects.filter(status='ativo')
        if self.request.user.is_staff == False:
            queryset = queryset.filter(status='ativo',usuario_fk=self.request.user.id)
        return queryset
    
    