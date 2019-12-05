# Generated by Django 2.2.7 on 2019-12-03 22:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('uc', models.IntegerField(blank=True, editable=False, null=True)),
                ('um', models.IntegerField(blank=True, editable=False, null=True)),
                ('descripcion', models.CharField(help_text='Nombre del servicio', max_length=45, unique=True, verbose_name='Nombre servicio')),
                ('hora_inicio', models.TimeField(help_text='Hora de inicio', verbose_name='Hora inicio')),
                ('hora_fin', models.TimeField(help_text='Hora de fin', verbose_name='Hora fin')),
                ('valor', models.PositiveIntegerField(help_text='Valor del servicio', verbose_name='Valor servicio')),
                ('lunes', models.BooleanField(default=True, help_text='El servicio se presta el lunes', verbose_name='Lunes')),
                ('martes', models.BooleanField(default=True, help_text='El servicio se presta el martes', verbose_name='martes')),
                ('miercoles', models.BooleanField(default=True, help_text='El servicio se presta el miércoles', verbose_name='Miercoles')),
                ('jueves', models.BooleanField(default=True, help_text='El servicio se presta el jueves', verbose_name='Jueves')),
                ('viernes', models.BooleanField(default=True, help_text='El servicio se presta el viernes', verbose_name='Viernes')),
                ('sabado', models.BooleanField(default=True, help_text='El servicio se presta el sábado', verbose_name='Sábado')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
            },
        ),
        migrations.CreateModel(
            name='Programacion_servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('uc', models.IntegerField(blank=True, editable=False, null=True)),
                ('um', models.IntegerField(blank=True, editable=False, null=True)),
                ('fecha', models.DateField(default=datetime.datetime(2019, 12, 3, 17, 28, 21, 568314), help_text='Fecha en que se programa prestar un servicio', verbose_name='Fecha programacion servicio')),
                ('servicio', models.ForeignKey(help_text='Servicio a programar', on_delete=False, to='ser.Servicio', verbose_name='Servicio a programar')),
            ],
            options={
                'verbose_name': 'Programación Servicio',
                'verbose_name_plural': 'Programación Servicios',
            },
        ),
    ]