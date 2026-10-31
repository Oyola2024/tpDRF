from rest_framework import serializers
from .models import Articulo, Proveedor

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = [
            'id',
            'nombre',
            'activo',
            'telefono',
            'timestamp',
        ]
        read_only_fields = ['id']

class ArticuloPublicSerializer(serializers.ModelSerializer):
    proveedor = ProveedorSerializer(read_only=True)

    class Meta:
        model = Articulo
        fields = [
            'id',
            'nombre',
            'descripcion',
            'precio',
            'proveedor',
        ]
        read_only_fields = ['id', 'timestamp']

class ArticuloSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Articulo
        fields = [
            'id',
            'nombre',
            'descripcion',
            'precio',
            'stock',
            'proveedor',
            'timestamp',
        ]
        read_only_fields = ['id', 'timestamp']
