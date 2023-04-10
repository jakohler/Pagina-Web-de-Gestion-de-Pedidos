from django.shortcuts import render
from blog.models import Post, Categoria

# Create your views here.

def blog(request):

    post = Post.objects.all()

    return render(request, "blog/blog.html", {'posts': post})

def categoria(request, categoria_id):

    categoria = Categoria.objects.get(id=categoria_id)    #filtrando la categoria buscada
    post = Post.objects.filter(categoria=categoria)     #filtrando todo los posts de esa categoria filtrada

    return render(request, "blog/categorias.html", {'categorias': categoria, 'posts': post})
