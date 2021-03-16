from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    # path('lista/', views.VideojuegoList.as_view(), name='lista_videojuegos'),
    path('nuevo/', views.NuevoUsuario.as_view(), name='nuevo_usuario'),
    path('municipios/<int:id_estado>', views.obtiene_municipios, name='obtiene_municipios'),
    # path('editar/<int:pk>', views.VideojuegoActualizar.as_view(), name='editar_videojuego'),
    # path('detalles/<int:pk>', views.VideojuegoDetalle.as_view(), name='detalles_videojuego'),
]