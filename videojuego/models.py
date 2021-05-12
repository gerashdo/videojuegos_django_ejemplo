# from django.db.models.fields.related import ForeignKey
#from videojuegos import usuarios
from django.db import models

class Videojuego(models.Model):
    # sin id
    titulo = models.CharField('Titulo', max_length=50, unique=True)
    anio = models.IntegerField('Año')
    categoria = models.ForeignKey("videojuego.Categoria", verbose_name='categoria', on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField('Stock')
    descripcion = models.CharField('Descripción',max_length=250, null=True, blank=True) 

    def __str__(self):
        return self.titulo

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

# class Venta(models.Model):
#     fecha
#     usuario

# class DetalleVenta(models.Model):
#     videojuego = models.ForeignKey("videojuego.Videojuego", verbose_name="Videojuego", on_delete=models.CASCADE)