from django.db import models

# Create your models here.
from bases.models import ClaseModelo


class Genero( ClaseModelo ):
    descripcion = models.CharField(
        max_length=45,
        help_text='Descripción del género',
        unique=True,
        verbose_name='Descripción género'
    )

    def __str__(self):
        return '{}'.format( self.descripcion )

    def save(self):
        self.descripcion = self.descripcion.upper()
        super( Genero, self ).save()

    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'


########################################################################################################################

class Documento( ClaseModelo ):
    descripcion = models.CharField(
        max_length=45,
        help_text='Descripción del documento de identidad',
        unique=True,
        verbose_name='Descripcion documento'
    )

    def save(self):
        self.descripcion = self.descripcion.upper()
        super( Documento, self ).save()

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = 'Documento de identidad'
        verbose_name_plural = 'Documentos de identidad'


########################################################################################################################
class Tipo_beneficiario( ClaseModelo ):
    descripcion = models.CharField(
        max_length=45,
        help_text='Descripción del tipo de beneficiario, ej: Estudiante Bachillerato',
        unique=True,
        verbose_name='Descripcion tipo beneficiario'
    )

    def save(self):
        self.descripcion = self.descripcion.upper()
        super( Tipo_beneficiario, self ).save()

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = 'Tipo de beneficiario'
        verbose_name_plural = 'Tipos de beneficiarios'


########################################################################################################################
class Dependencia( ClaseModelo ):
    descripcion = models.CharField(
        max_length=45,
        help_text='Descripcion de la dependencia a la que pertenece, ej: Sistemas, Vigilancia',
        unique=True,
        verbose_name='Descripcion dependencia'
    )

    def save(self):
        self.descripcion = self.descripcion.upper()
        super( Dependencia, self ).save()

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = 'Dependencia'
        verbose_name_plural = 'Dependencias'


########################################################################################################################

class Beneficiario( ClaseModelo ):
    rfid = models.CharField(
        max_length=10,
        help_text='RFID carné o llavero    ',
        unique=True,
        verbose_name='RFID'
    )

    documento = models.ForeignKey(
        Documento,
        help_text='Documento de identidad del beneficiario',
        verbose_name='Documento de identidad',
        on_delete=False
    )

    numero_documento = models.CharField(
        max_length=15,
        help_text='Número del documento de identidad del beneficiario',
        unique=True,
        verbose_name='Número de documento'
    )

    genero = models.ForeignKey(
        Genero,
        help_text='Gérero del beneficiario',
        verbose_name='Género',
        on_delete=False
    )

    dependencia = models.ForeignKey(
        Dependencia,
        help_text='Dependencia a la que pertenece',
        verbose_name='Dependencia',
        on_delete=False
    )

    tipo_beneficiario = models.ForeignKey(
        Tipo_beneficiario,
        help_text='Tipo de beneficiario',
        verbose_name='Tipo beneficiario',
        on_delete=False
    )

    nombres = models.CharField(
        max_length=45,
        # help_text='Nombres del beneficiario',
        verbose_name='Nombres'
    )

    apellidos = models.CharField(
        max_length=45,
        # help_text='Apellidos del beneficiario',
        verbose_name='Apellidos'
    )

    email = models.EmailField(
        max_length=70,
        # help_text='Correo electrónico del beneficiario',
        verbose_name='Correo electrónico',
        unique=True
    )

    fecha_nacimiento = models.DateField(
        help_text='<em>AAAA-MM-DD</em>',
        verbose_name='Fecha de nacimiento'
    )

    saldo = models.IntegerField(
        verbose_name='Saldo',
        default=0,
        editable=False
    )

    foto = models.ImageField(
        upload_to='beneficiarios'
    )

    def save(self):
        self.rfid = self.rfid.upper()
        self.nombres = self.nombres.upper()
        self.apellidos = self.apellidos.upper()
        super( Beneficiario, self ).save()

    def __str__(self):
        return '{}'.format( self.rfid )

    class Meta:
        verbose_name = 'Beneficiario'
        verbose_name_plural = 'Beneficiarios'
