# Generated by Django 2.2.7 on 2019-12-04 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ben', '0002_auto_20191202_2204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recarga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('uc', models.IntegerField(blank=True, editable=False, null=True)),
                ('um', models.IntegerField(blank=True, editable=False, null=True)),
                ('valor', models.PositiveIntegerField(help_text='Valor recarga', verbose_name='Valor recarga')),
                ('beneficiario', models.ForeignKey(help_text='Nombre del beneficiario', on_delete=False, to='ben.Beneficiario', verbose_name='Nombre beneficiario')),
            ],
            options={
                'verbose_name': 'Recarga',
                'verbose_name_plural': 'Recargas',
            },
        ),
    ]
