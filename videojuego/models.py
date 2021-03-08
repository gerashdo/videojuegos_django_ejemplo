from django.db import models

class Videojuego(models.Model):
    # sin id
    titulo = models.CharField('Titulo', max_length=50, unique=True)
    anio = models.IntegerField('Año')
    categoria = models.ForeignKey("videojuego.Categoria", verbose_name='categoria', on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    descripcion = models.CharField('Descripción',max_length=250, null=True, blank=True) 

    def __str__(self):
        return self.titulo

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre