from django.shortcuts import render
from .models import Setor
from .serializers import SetorSerializer
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

class SetorViewSet(viewsets.ModelViewSet):
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
         instance.status = 'desativado'
         instance.save()

    def get_queryset(self):
         return super().get_queryset().filter(status='ativo')
    
    def get_permissions(self):
         return [permissions.IsAdminUser()]