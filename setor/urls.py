from django.urls import path, include
from rest_framework.routers import DefaultRouter
from setor.views import SetorViewSet

router = DefaultRouter()
router.register(r'',SetorViewSet)

urlpatterns = [
    path('',include(router.urls))
]
