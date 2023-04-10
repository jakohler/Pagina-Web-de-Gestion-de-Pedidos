from django.db import models

# Create your models here.

class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=50)
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoriaProductos'
        verbose_name_plural = 'categoriasProductos'
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='tienda', null=True, blank=True)
    disponibilidad = models.BooleanField(default=True)
    categoria = models.ManyToManyField(CategoriaProducto)      #creando una relacion de tablas varios a varios con producto y CategoriaProducto
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'produtco'
        verbose_name_plural = 'productos'
    
    def __str__(self):
        return self.nombre