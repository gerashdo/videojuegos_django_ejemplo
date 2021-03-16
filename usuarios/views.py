from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from .models import Usuario, Estado, Municipio
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.http import JsonResponse

class NuevoUsuario(CreateView):
    model = Usuario
    form_class = UsuarioForm
    extra_context = {'etiqueta':'Nuevo','boton':'Agregar'}
    success_url = reverse_lazy('videojuego:lista_videojuegos')

def obtiene_municipios(request, id_estado):
    municipios = Municipio.objects.filter(estado_id=id_estado)

    json = []

    for municipio in municipios:
        json.append({'id':municipio.id, 'nombre':municipio.nombre})

    return JsonResponse(json, safe=False)
