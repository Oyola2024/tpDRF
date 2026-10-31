from django.db import models

    
# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    telefono = models.CharField(max_length=70)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Proveedor: {self.nombre} - Activo: {self.activo} - Telefono: {self.telefono}"
    
class Articulo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.IntegerField()
    stock = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='articulos')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre