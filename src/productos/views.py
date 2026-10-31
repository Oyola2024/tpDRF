from .models import Articulo, Proveedor
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import ArticuloSerializer, ProveedorSerializer




class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all().select_related("proveedor")
    serializer_class = ArticuloSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['post'])
    def publicar(self, request, pk=None):
        articulo = self.get_object()
        articulo.estado = 'Publicado'
        articulo.save()
        return Response({'status': 'Artículo publicado exitosamente'})
        
    # detail=False significa que aplica a la colección entera
    # Ejemplo: /articulos/recientes/
    @action(detail=False, methods=['get'])
    def recientes(self, request):
        recientes = Articulo.objects.order_by('-fecha_creacion')[:5]
        serializer = self.get_serializer(recientes, many=True)
        return Response(serializer.data)


# #------------------

class ProveedorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]