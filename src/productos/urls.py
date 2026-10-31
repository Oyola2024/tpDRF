from django.urls import path
from .views import ArticulosDetailGenericAPIView, ProveedoresAPIView, ProveedorDetailAPIView, ArticulosGenericAPIView

urlpatterns = [
    path('articulos/', ArticulosGenericAPIView.as_view(), name='articulos_api'),
    path('articulos/<int:pk>/', ArticulosDetailGenericAPIView.as_view(), name='articulo_detail'),
    path('proveedores/', ProveedoresAPIView.as_view(), name='proveedores_api'),
    path('proveedores/<int:pk>/', ProveedorDetailAPIView().as_view(), name='proveedor_detail'),
]