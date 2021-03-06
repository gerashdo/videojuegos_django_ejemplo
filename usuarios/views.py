import functools

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from .token import token_activacion
from django.views.generic import ListView
from .models import Usuario, Estado, Municipio
from .forms import UsuarioForm, UsuarioRegistroForm, UsuarioActualizarForm
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.views.generic import TemplateView
from django.contrib import messages
from django_weasyprint import WeasyTemplateResponseMixin
from django_weasyprint.views import CONTENT_TYPE_PNG, WeasyTemplateResponse
from django.conf import settings
from django.contrib.auth.models import Group
from django import template

class NuevoUsuario(CreateView):
    model = Usuario
    form_class = UsuarioForm
    extra_context = {'etiqueta':'Nuevo','boton':'Agregar'}
    success_url = reverse_lazy('usuarios:lista_usuario')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = True
        user.save()
        grupo = Group.objects.get(name='usuario') 
        user.groups.add(grupo)
        return super().form_valid(form)

class UsuarioRegistro(CreateView):
    template_name = 'signup.html'
    model = Usuario
    form_class = UsuarioRegistroForm
    success_url = reverse_lazy('usuarios:login_usuario')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        grupo = Group.objects.get(name='usuario') 
        user.groups.add(grupo)

        dominio = get_current_site(self.request)
        uid = urlsafe_base64_encode(force_bytes(user.id))
        token = token_activacion.make_token(user)
        mensaje = render_to_string('confirmar_cuenta.html',
            {
                'usuario': user,
                'dominio': dominio,
                'uid': uid,
                'token': token
            }
        )
        asunto = 'Activa Cuenta Videojuegos'
        to = user.email
        email = EmailMessage(
            asunto,
            mensaje,
            to = [to]
        )
        email.content_subtype = 'html'
        email.send()

        return super().form_valid(form)

class ActivarCuenta(TemplateView):
    def get(self, request, *args, **kwargs):
        try:
            uid = urlsafe_base64_decode(kwargs['uid64'])
            token = kwargs['token']
            user = Usuario.objects.get(id=uid)
        except:
            user = None
        
        if user and token_activacion.check_token(user,token):
            user.is_active = True
            user.save()
            messages.success(self.request, 'Cuenta activada con ??xito.')
        else:
            messages.error(self.request, 'Token invalido, contacta al administrador')
        
        return redirect('usuarios:login_usuario')

def obtiene_municipios(request):
    if request.method == 'GET':
        return JsonResponse({'error':'Peticion incorrecta'}, safe=False, status=403)
    id_estado = request.POST.get('id')
    municipios = Municipio.objects.filter(estado_id=id_estado)

    json = []
    if not municipios:
        json.append({'error':'No se encontraron municipios para ese estado'})
    
    for municipio in municipios:
        json.append({'id':municipio.id, 'nombre':municipio.nombre})

    return JsonResponse(json, safe=False)

class UsuarioList(ListView):
    model = Usuario
    # usuario = Group.objects.get(name='usuario')
    # administrador = Group.objects.get(name='administrador')
    grupos = Group.objects.all()
    # extra_context = {'usuario_grupo':usuario, 'admin_grupo':administrador}
    extra_context = {'grupos':grupos}

class UsuarioEliminar(DeleteView):
    model = Usuario
    success_url = reverse_lazy('usuarios:lista_usuario')

class UsuarioActualizar(UpdateView):
    model = Usuario
    form_class = UsuarioActualizarForm
    extra_context = {'etiqueta':'Editar','boton':'Guardar'}
    success_url = reverse_lazy('usuarios:lista_usuario')

class UsuarioDetalle(DetailView):
    model = Usuario

class UsuarioLogin(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    
    def get_success_url(self):
        self.request.session['cuantos'] = 0
        self.request.session['total'] = 0.0
        self.request.session['videojuegos'] = {}
        return super().get_success_url()

def UsuarioDarUsuario(request,pk):
    usuario = Usuario.objects.get(id=pk)
    grupo = Group.objects.get(name='usuario') 
    usuario.groups.add(grupo)
    return redirect('usuarios:lista_usuario')

def UsuarioDarAdministrador(request,pk):
    usuario = Usuario.objects.get(id=pk)
    grupo = Group.objects.get(name='administrador') 
    usuario.groups.add(grupo)
    return redirect('usuarios:lista_usuario')

def UsuarioModificarGrupo(request, user_id, grupo_id, opcion):
    grupo = Group.objects.get(id=grupo_id)
    usuario = Usuario.objects.get(id=user_id)
    if opcion == 0:
        if grupo not in usuario.groups.all():
            messages.error(request, f'El usuario {usuario.username} no pertenece al grupo {grupo.name}.')
        else:
            if usuario.groups.count() <= 1:
                messages.error(request, f'El usuario {usuario.username} no puede quedar sin un grupo.')
            else:
                usuario.groups.remove(grupo)
                messages.success(request, f'El usuario {usuario.username} ya no pertenece al grupo {grupo.name}.')
    elif opcion == 1:
        if grupo in usuario.groups.all():
            messages.error(request, f'El usuario {usuario.username} ya pertenece al grupo {grupo.name}.')
        else:
            usuario.groups.add(grupo)
            messages.success(request, f'El usuario {usuario.username} pertenece al grupo {grupo.name}.')

    return redirect('usuarios:lista_usuario')

class VistaPdf(ListView):
    model = Usuario
    template_name = 'usuarios/usuario_pdf.html'

class UsuarioListPdf(WeasyTemplateResponseMixin, VistaPdf):
    # output of MyModelView rendered as PDF with hardcoded CSS
    pdf_stylesheets = [
        settings.STATICFILES_DIRS[0] + '/css/portal.css',
        settings.STATICFILES_DIRS[0] + '/css/estilos.css',
    ]
    # show pdf in-line (default: True, show download dialog)
    pdf_attachment = False
    # custom response class to configure url-fetcher
    pdf_name = 'foo.pdf'

