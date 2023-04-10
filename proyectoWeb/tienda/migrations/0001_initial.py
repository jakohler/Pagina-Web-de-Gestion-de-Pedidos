# Generated by Django 4.1.7 on 2023-04-05 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('actualizacion', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'categoriaProductos',
                'verbose_name_plural': 'categoriasProductos',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.FloatField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='tienda')),
                ('disponibilidad', models.BooleanField(default=True)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('actualizacion', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.ManyToManyField(to='tienda.categoriaproducto')),
            ],
            options={
                'verbose_name': 'produtco',
                'verbose_name_plural': 'productos',
            },
        ),
    ]
