from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Videojuego
from .form_categoria import CategoriaForm, VideojuegoForm
#from .form_videojuego import VideojuegoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

# CATEGORIAS
def lista_categoria(request):
    categorias= Categoria.objects.all()
    return render(request,'categorias/lista_categorias.html',{'categorias':categorias})

def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    return redirect('categoria:lista_categoria')

def editar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    form = CategoriaForm(instance=categoria)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categoria:lista_categoria')
    context = {
        'form' : form,
        'etiqueta' : 'Editar',
        'boton' : 'Guardar',
    }     
    return render(request,'categorias/form_categoria.html',context)

def nuevo_categoria(request):
    form = CategoriaForm

    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria:lista_categoria')

    context = {
        'form' : form,
        'etiqueta' : 'Nueva',
        'boton' : 'Agregar',
    }
    return render(request,'categorias/form_categoria.html',context)


# VIDEOJUEGOS

# def lista_videojuegos(request):
#     videojuegos = Videojuego.objects.all()
#     return render(request,'lista_videojuegos.html',{'videojuegos':videojuegos})

# def eliminar_videojuego(request, id):
#     videojuego = Videojuego.objects.get(id=id)
#     videojuego.delete()
#     return redirect('videojuego:lista_videojuegos')

# def nuevo_videojuego(request):
#     form = VideojuegoForm

#     if request.method == 'POST':
#         form = VideojuegoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('videojuego:lista_videojuegos')

#     context = {
#         'form' : form
#     }
#     return render(request,'nuevo_videojuego.html', context)

# def editar_videojuego(request, id):
#     videojuego = Videojuego.objects.get(id=id)
#     form = VideojuegoForm(instance=videojuego)

#     if request.method == 'POST':
#         form = VideojuegoForm(request.POST, instance=videojuego)
#         if form.is_valid():
#             form.save()
#             return redirect('videojuego:lista_videojuegos')

#     context = {
#         'form' : form
#     }
#     return render(request, 'editar_videojuego.html', context)

class VideojuegoList(ListView):
    model = Videojuego
    #extra_context = {'vj-lista':True}
    #queryset = Videojuego.objects.filter(anio=1992)

class VideojuegoEliminar(DeleteView):
    model = Videojuego
    success_url = reverse_lazy('videojuego:lista_videojuegos')

# class VideojuegoCrear(CreateView):
#     model = Videojuego
#     fields = '__all__'
#     extra_context = {'etiqueta':'Nuevo', 'boton':'Agregar'}
#     success_url = reverse_lazy('videojuego:lista_videojuegos')

class VideojuegoCrear(CreateView):
    model = Videojuego
    form_class = VideojuegoForm
    extra_context = {'etiqueta':'Nuevo', 'boton':'Agregar'}
    success_url = reverse_lazy('videojuego:lista_videojuegos')


# class VideojuegoActualizar(UpdateView):
#     model = Videojuego
#     fields = '__all__'
#     extra_context = {'etiqueta':'Actualizar', 'boton':'Guardar'}
#     success_url = reverse_lazy('videojuego:lista_vidojuegos')

class VideojuegoActualizar(UpdateView):
    model = Videojuego
    form_class = VideojuegoForm
    extra_context = {'etiqueta':'Actualizar', 'boton':'Guardar'}
    success_url = reverse_lazy('videojuego:lista_vidojuegos')

class VideojuegoDetalle(DetailView):
    model = Videojuego