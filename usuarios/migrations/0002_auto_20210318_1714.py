# Generated by Django 3.1.7 on 2021-03-18 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='perfiles', verbose_name='Foto de perfil'),
        ),
    ]