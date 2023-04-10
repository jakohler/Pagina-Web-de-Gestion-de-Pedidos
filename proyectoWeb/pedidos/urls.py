from django.urls import path
from . import views

urlpatterns = [
    path('', views.procesarPedido, name="procesar_pedido"),
]

