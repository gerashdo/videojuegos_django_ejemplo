from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'usuarios'

urlpatterns = [
    path('lista/', views.UsuarioList.as_view(), name='lista_usuario'),
    path('lista-pdf/', views.UsuarioListPdf.as_view(), name='lista_pdf_usuario'),
    path('nuevo/', views.NuevoUsuario.as_view(), name='nuevo_usuario'),
    path('municipios/', views.obtiene_municipios, name='obtiene_municipios'),
    path('activar/<slug:uid64>/<slug:token>', views.ActivarCuenta.as_view(), name='activar_cuenta'),
    path('eliminar/<int:pk>', views.UsuarioEliminar.as_view(), name='eliminar_usuario'),
    path('editar/<int:pk>', views.UsuarioActualizar.as_view(), name='editar_usuario'),
    path('detalles/<int:pk>', views.UsuarioDetalle.as_view(), name='detalles_usuario'),
    path('login/', views.UsuarioLogin.as_view(), name='login_usuario'),
    path('registro/', views.UsuarioRegistro.as_view(), name='registro_usuario'),
    path('dar-usuario/<int:pk>', views.UsuarioDarUsuario, name='dar_usuario_usuario'),
    path('dar-administrador/<int:pk>', views.UsuarioDarAdministrador, name='dar_administrador_usuario'),
    path('modificar-grupo/<int:user_id>/<int:grupo_id>/<int:opcion>', views.UsuarioModificarGrupo, name='modificar_grupo_usuario'),
    path("logout/", LogoutView.as_view(), name="logout"),
]