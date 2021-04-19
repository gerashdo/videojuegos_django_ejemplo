from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Videojuego
from .form_categoria import CategoriaForm, VideojuegoForm
#from .form_videojuego import VideojuegoForm
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.db.models import Count
from django_weasyprint import WeasyTemplateResponseMixin
from django.conf import settings

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
    paginate_by = 1
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

class Grafica(TemplateView):
    template_name = 'videojuego/grafica.html'
    
    def get(self, request, *args, **kwargs):
        vide_categoria = Videojuego.objects.all().values('categoria').annotate(cuantos=Count('categoria'))
        categorias = Categoria.objects.all()
    
        datos = []
        for categoria in categorias:
            cuantos = 0
            for vid_cat in vide_categoria: 
                if vid_cat['categoria'] == categoria.id:
                    cuantos = vid_cat['cuantos']
                    break
            datos.append({'name':categoria.nombre, 'data':[cuantos]})
    
        self.extra_context = {'datos': datos}
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

class VistaPdf(ListView):
    model = Videojuego
    template_name = 'videojuego/videojuego_lista_pdf.html'

class VideojuegoListPdf(WeasyTemplateResponseMixin, VistaPdf):
    # output of MyModelView rendered as PDF with hardcoded CSS
    pdf_stylesheets = [
        settings.STATICFILES_DIRS[0] + '/css/portal.css',
        settings.STATICFILES_DIRS[0] + '/css/estilos.css',
    ]
    # show pdf in-line (default: True, show download dialog)
    pdf_attachment = False
    # custom response class to configure url-fetcher
    pdf_name = 'Videojuegos.pdf'

class VistaVideojuegoDetallePdf(DetailView):
    model = Videojuego
    template_name = 'videojuego/videojuego_Detalle_pdf.html'

class VideojuegoDetallePdf(WeasyTemplateResponseMixin, VistaVideojuegoDetallePdf):
     # output of MyModelView rendered as PDF with hardcoded CSS
    pdf_stylesheets = [
        settings.STATICFILES_DIRS[0] + '/css/portal.css',
        settings.STATICFILES_DIRS[0] + '/css/estilos.css',
    ]
    # show pdf in-line (default: True, show download dialog)
    pdf_attachment = False
    # custom response class to configure url-fetcher
    pdf_name = 'Videojuego_Detalle.pdf'