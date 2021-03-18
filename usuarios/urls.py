from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('lista/', views.UsuarioList.as_view(), name='lista_usuario'),
    path('nuevo/', views.NuevoUsuario.as_view(), name='nuevo_usuario'),
    path('municipios/', views.obtiene_municipios, name='obtiene_municipios'),
    # path('editar/<int:pk>', views.VideojuegoActualizar.as_view(), name='editar_videojuego'),
    # path('detalles/<int:pk>', views.VideojuegoDetalle.as_view(), name='detalles_videojuego'),
]