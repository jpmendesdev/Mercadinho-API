from django.shortcuts import render
from rest_framework import viewsets,permissions
from vendas.models import Venda
from vendas.serializers import VendaSerializer


class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

    def perform_destroy(self, instance):
        instance.status = instance.STATUS['des']
        instance.save()

    def get_queryset(self):
        return super().get_queryset().filter(status='ativo')
    