from django.shortcuts import render
from .models import Articulo
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializers import ArticuloSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def articulos(request):
    if request.method == 'GET':
        articulos = Articulo.objects.all()
        serializer = ArticuloSerializer(articulos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = ArticuloSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Articulo creado"}, status=status.HTTP_201_CREATED)
        return Response({"mensaje":"No se creó oirque no es válido"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def articulo_detail(request, pk):
    if request.method == 'GET':
        articulo = get_object_or_404(Articulo, pk=pk)
        serializer = ArticuloSerializer(articulo)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        articulo = get_object_or_404(Articulo, pk=pk)
        serializer = ArticuloSerializer(articulo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Articulo actualizado"}, status=status.HTTP_200_OK)
        return Response({"mensaje": "No se actualizó porque no es válido"}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        articulo = get_object_or_404(Articulo, pk=pk)
        articulo.delete()
        return Response({"mensaje": "Articulo eliminado"}, status=status.HTTP_204_NO_CONTENT)