from django.urls import path
from . import views

app_name = 'videojuego'

urlpatterns = [
    path('lista/', views.VideojuegoList.as_view(), name='lista_videojuegos'),
    path('nuevo/', views.VideojuegoCrear.as_view(), name='nuevo_videojuego'),
    path('eliminar/<int:pk>', views.VideojuegoEliminar.as_view(), name='eliminar_videojuego'),
    path('editar/<int:pk>', views.VideojuegoActualizar.as_view(), name='editar_videojuego'),
    path('detalles/<int:pk>', views.VideojuegoDetalle.as_view(), name='detalles_videojuego'),
    path('grafica/', views.Grafica.as_view(), name='grafica_videojuego'),
    path('lista-pdf/', views.VideojuegoListPdf.as_view(), name='lista_pdf_videojuego'),
    path('vidojuego-pdf/<int:pk>', views.VideojuegoDetallePdf.as_view(), name='detalle_pdf_videojuego'),
    path('lista-compra', views.VideojuegoCompraList.as_view(), name='lista_compra_videojuego'),
    path('comprar/<int:pk>', views.videojuego_comprar, name='comprar_videojuego'),
]
