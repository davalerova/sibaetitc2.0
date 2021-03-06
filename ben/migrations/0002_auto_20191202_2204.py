# Generated by Django 2.2.7 on 2019-12-03 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ben', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiario',
            name='uc',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='beneficiario',
            name='um',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='dependencia',
            name='uc',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='dependencia',
            name='um',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='documento',
            name='uc',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='documento',
            name='um',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='genero',
            name='uc',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='genero',
            name='um',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='tipo_beneficiario',
            name='uc',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='tipo_beneficiario',
            name='um',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]
