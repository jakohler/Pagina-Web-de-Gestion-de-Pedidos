from django.contrib import admin
from .models import Categoria, Post

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)