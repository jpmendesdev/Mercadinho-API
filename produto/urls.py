from rest_framework import routers
from produto.views import ProdutoViewSet
from django.urls import path,include

router = routers.DefaultRouter()
router.register(r'',ProdutoViewSet)

urlpatterns = [
    path('',include(router.urls)),
]