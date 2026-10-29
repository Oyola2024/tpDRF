from django.urls import path
from .views import articulos, articulo_detail

urlpatterns = [
    path('', articulos, name='articulos'),
    path('<int:pk>/', articulo_detail, name='articulo_detail'),
]