# from django.db.models.fields.related import ForeignKey
#from videojuegos import usuarios
from django.db import models
from django.db.models.fields.related import ForeignKey

class Videojuego(models.Model):
    # sin id
    titulo = models.CharField('Titulo', max_length=50, unique=True)
    anio = models.IntegerField('Año')
    categoria = models.ForeignKey("videojuego.Categoria", verbose_name='categoria', on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField('Stock')
    descripcion = models.CharField('Descripción',max_length=250, null=True, blank=True) 

    def __str__(self):
        return self.titulo

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    fecha = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey("usuarios.Usuario", verbose_name='Usuario', on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=8, decimal_places=2)

class DetalleVenta(models.Model):
    venta = models.ForeignKey("videojuego.Venta", verbose_name='Venta', on_delete=models.CASCADE)
    id_videojuego = models.IntegerField('ID_Videojuego')
    titulo_videojuego = models.CharField('Titulo', max_length=50)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    cantidad = models.IntegerField('cantidad')
    total = models.DecimalField(max_digits=7, decimal_places=2)