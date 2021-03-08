from django.urls import path
from . import views

app_name = 'videojuego'

urlpatterns = [
    path('lista/', views.VideojuegoList.as_view(), name='lista_videojuegos'),
    path('nuevo/', views.VideojuegoCrear.as_view(), name='nuevo_videojuego'),
    path('eliminar/<int:pk>', views.VideojuegoEliminar.as_view(), name='eliminar_videojuego'),
    path('editar/<int:pk>', views.VideojuegoActualizar.as_view(), name='editar_videojuego'),
    path('detalles/<int:pk>', views.VideojuegoDetalle.as_view(), name='detalles_videojuego'),
]