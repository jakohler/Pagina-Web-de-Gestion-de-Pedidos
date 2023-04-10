from django.shortcuts import render, redirect
from .carro import Carro
from tienda.models import Producto

# Create your views here.

def agregarProducto(request, producto_id):
    carro = Carro(request)           #creando nuestro objeto Carro
    producto = Producto.objects.get(id=producto_id)  #buscamos el producto segun el id
    carro.agregar(producto=producto)

    return redirect("tienda")

def eliminarProducto(request, producto_id):
    carro = Carro(request)           
    producto = Producto.objects.get(id=producto_id)  
    carro.eliminar(producto=producto)

    return redirect("tienda")

def restarProducto(request, producto_id):
    carro = Carro(request)           
    producto = Producto.objects.get(id=producto_id) 
    carro.restarProducto(producto=producto)

    return redirect("tienda")

def limpiarCarro(request):
    carro = Carro(request)           
    carro.limpiarCarro()

    return redirect("tienda")