from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('lista/', views.UsuarioList.as_view(), name='lista_usuario'),
    path('nuevo/', views.NuevoUsuario.as_view(), name='nuevo_usuario'),
    path('municipios/', views.obtiene_municipios, name='obtiene_municipios'),
    path('eliminar/<int:pk>', views.UsuarioEliminar.as_view(), name='eliminar_usuario'),
    #path('editar/<int:pk>', views.UsuarioActualizar.as_view(), name='editar_usuario'),
    #path('detalles/<int:pk>', views.UsuarioDetalle.as_view(), name='detalles_usuario'),
]