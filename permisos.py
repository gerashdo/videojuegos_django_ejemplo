import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','videojuegos.settings')
django.setup()

from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from usuarios.models import Usuario

grupo_administrador = Group.objects.create(name='administrador')
grupo_usuario = Group.objects.create(name='usuario')

content_type = ContentType.objects.get_for_model(Usuario)

permiso_usuarios = Permission.objects.create(
    codename = 'permiso_usuario',
    name = 'Permiso requerido para el grupo usuario',
    content_type = content_type
)

permiso_administradores = Permission.objects.create(
    codename = 'permiso_administrador',
    name = 'Permiso requerido para el grupo administrador',
    content_type = content_type
)

grupo_usuario.permissions.add(permiso_usuarios)
grupo_administrador.permissions.add(permiso_administradores)

