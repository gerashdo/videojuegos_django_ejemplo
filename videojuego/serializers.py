from .models import Videojuego, Categoria
from rest_framework import serializers


class VideojuegoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Videojuego
        fields = ['id', 'titulo', 'anio', 'categoria', 'precio', 'descripcion']


class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre']