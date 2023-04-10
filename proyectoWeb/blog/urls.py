from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name="blog"),    #no es necesario agregarle el primer argumento a path porque ya estamos en la carpeta raiz de la view
    path('categoria/<int:categoria_id>', views.categoria, name='categoria')
]