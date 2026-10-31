from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticuloViewSet, ProveedorViewSet

router = DefaultRouter()

router.register(r'articulos', ArticuloViewSet, basename='articulos')
router.register(r'proveedores', ProveedorViewSet, basename='proveedores')

urlpatterns = [
    path('', include(router.urls)),
]