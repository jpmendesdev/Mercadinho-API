from django.urls import path, include
from rest_framework.routers import DefaultRouter
from vendas.views import VendaViewSet

router = DefaultRouter()
router.register(r'',VendaViewSet)

urlpatterns = [
    path('',include(router.urls))
]