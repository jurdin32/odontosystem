from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
from django.forms import model_to_dict


class Paciente(models.Model):
    cedula = models.CharField(max_length=10, verbose_name='Cedula', primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre', null=True, blank=True)
    apellido = models.CharField(max_length=50, verbose_name='Apellido', null=True, blank=True)
    direccion = models.CharField(max_length=100, verbose_name='Direccion', null=True, blank=True)
    ocupacion = models.CharField(max_length=100, verbose_name='Ocupaciòn', null=True, blank=True)
    sexo = models.CharField(max_length=20, verbose_name='Sexo', null=True, blank=True)
    telefono = models.CharField(max_length=10, verbose_name='Telefono', null=True, blank=True)
    fechaNacimiento = models.DateField(default=datetime.now, verbose_name='Fecha de nacimiento', null=True, blank=True)

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'tb_paciente'
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering = ['cedula']


class AntecedentesPatologicos(models.Model):
    cedula = models.OneToOneField(Paciente, on_delete=models.CASCADE, primary_key=True)
    enfermedadesCardiacas=models.CharField(max_length=200, verbose_name='Enfermedades Cardiacas', null=True, blank=True)
    presionArterial=models.CharField(max_length=1, verbose_name='Presion Arterial', null=True, blank=True)
    transtornosSanguineos=models.CharField(max_length=200, verbose_name='Transtornos Sanguineos', null=True, blank=True)
    alergias=models.CharField(max_length=200, verbose_name='Alergias', null=True, blank=True)
    medicacion=models.CharField(max_length=200, verbose_name='Medicacion', null=True, blank=True)
    otrasEnfermedades=models.CharField(max_length=200, verbose_name='Otras Enfermedades', null=True, blank=True)

    def __str__(self):
        return self.cedula.nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'tb_antecedentesPatologicos'
        verbose_name = 'Antecedente Patologico'
        verbose_name_plural = 'Antecedentes Patologicos'
        ordering = ['cedula']


class SintomatologiaOral(models.Model):
    cedula = models.OneToOneField(Paciente, on_delete=models.CASCADE, primary_key=True)
    halitosis=models.CharField(max_length=1, verbose_name='halitosis', null=True, blank=True)
    hipersensibilidad=models.CharField(max_length=5, verbose_name='hipersensibilidad', null=True, blank=True)
    sangradoEncias=models.CharField(max_length=1, verbose_name='sangrado Encias', null=True, blank=True)
    xerostomia=models.CharField(max_length=1, verbose_name='xerostomia', null=True, blank=True)
    bruxismo=models.CharField(max_length=1, verbose_name='bruxismo', null=True, blank=True)

    def __str__(self):
        return self.cedula.nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'tb_sintomatologiaOral'
        verbose_name = 'Sintomatologia Oral'
        verbose_name_plural = 'Sintomatologias Orales'
        ordering = ['cedula']


class Personal(models.Model):
    cedula=models.CharField(max_length=10,unique=True, verbose_name='cedula', null=True, blank=True)
    nombre=models.CharField(max_length=50, verbose_name='nombre', null=True, blank=True)
    apellido=models.CharField(max_length=50, verbose_name='apellido', null=True, blank=True)
    direccion=models.CharField(max_length=100, verbose_name='direccion', null=True, blank=True)
    titulo=models.CharField(max_length=100, verbose_name='titulo', null=True, blank=True)
    fechaIngreso=models.DateField(max_length=20, verbose_name='fecha Ingreso', null=True, blank=True)
    sexo=models.CharField(max_length=20, verbose_name='sexo', null=True, blank=True)
    telefono=models.CharField(max_length=10, verbose_name='telefono', null=True, blank=True)
    fechaNacimiento=models.DateField(default=datetime.now, verbose_name='Fecha de nacimiento', null=True, blank=True)

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'tb_personal'
        verbose_name = 'Personal'
        verbose_name_plural = 'Personales'
        ordering = ['id']


class Permisos(models.Model):
    usuario=models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    tipo=models.CharField(max_length=1, verbose_name='tipo', null=True, blank=True)
    foto=models.ImageField(upload_to="imagenes", verbose_name='foto', null=True, blank=True)

    def __str__(self):
        return self.usuario.username

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'tb_permisos'
        verbose_name = 'Permiso'
        verbose_name_plural = 'Permisos'
        ordering = ['usuario']


class Consultas(models.Model):
    personal=models.CharField(max_length=100, verbose_name='personal', null=True, blank=True)
    paciente=models.CharField(max_length=100, verbose_name='paciente', null=True, blank=True)
    fecha=models.CharField(max_length=10, verbose_name='fecha', null=True, blank=True)
    motivo=models.CharField(max_length=200, verbose_name='motivo', null=True, blank=True)
    diagnostico=models.CharField(max_length=200, verbose_name='diagnostico', null=True, blank=True)

    def __str__(self):
        return self.paciente

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'tb_consultas'
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
        ordering = ['id']


class Tratamiento(models.Model):
    personal=models.CharField(max_length=100, verbose_name='personal', null=True, blank=True)
    paciente=models.CharField(max_length=100, verbose_name='paciente', null=True, blank=True)
    fechaInicio=models.DateField(default=datetime.now, verbose_name='Fecha de inicio', null=True, blank=True)
    odontograma=models.CharField(max_length=5000, verbose_name='odontograma', null=True, blank=True)
    estado=models.CharField(max_length=2, verbose_name='estado', null=True, blank=True)
    costo=models.CharField(max_length=50, verbose_name='costo', null=True, blank=True)
    saldo=models.CharField(max_length=50, verbose_name='saldo', null=True, blank=True)

    def __str__(self):
        return self.paciente

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'tb_tratamiento'
        verbose_name = 'Tratamiento'
        verbose_name_plural = 'Tratamientos'
        ordering = ['id']


class DetalleTratamiento(models.Model):
    tratamiento=models.OneToOneField(Tratamiento, on_delete=models.CASCADE, primary_key=True)#clave forane de tratamiento
    personal=models.CharField(max_length=200, verbose_name='personal', null=True, blank=True)
    fecha=models.DateField(default=datetime.now, verbose_name='Fecha', null=True, blank=True)
    pieza=models.CharField(max_length=200, verbose_name='pieza', null=True, blank=True)
    diagnosticoTratamiento=models.CharField(max_length=200, verbose_name='diagnostico Tratamiento', null=True, blank=True)
    tratamientoRealizado=models.CharField(max_length=200, verbose_name='tratamiento Realizado', null=True, blank=True)

    def __str__(self):
        return self.tratamiento.paciente

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'tb_detalleTratamiento'
        verbose_name = 'Detalle Tratamiento'
        verbose_name_plural = 'Detalles Tratamientos'
        ordering = ['tratamiento']


class Pago(models.Model):
    cedula=models.CharField(max_length=2000, verbose_name='cedula', null=True, blank=True)
    fechaPagos=models.CharField(max_length=10, verbose_name='fecha Pagos', null=True, blank=True)
    tipo=models.CharField(max_length=2, verbose_name='tipo', null=True, blank=True)
    concepto=models.CharField(max_length=200, verbose_name='concepto', null=True, blank=True)
    monto=models.CharField(max_length=10, verbose_name='monto', null=True, blank=True)
    observaciones=models.CharField(max_length=200, verbose_name='observaciones', null=True, blank=True)

    def __str__(self):
        return self.cedula

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'tb_pago'
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'
        ordering = ['id']


class Turnos(models.Model):
    paciente=models.CharField(max_length=15, verbose_name='paciente', null=True, blank=True)
    fechaT=models.CharField(max_length=10, verbose_name='fecha', null=True, blank=True)
    horaT=models.CharField(max_length=20, verbose_name='hora', null=True, blank=True)
    estadoT=models.CharField(max_length=10, verbose_name='estado', null=True, blank=True)
    enunciado=models.CharField(max_length=20, verbose_name='enunciado', null=True, blank=True)

    def __str__(self):
        return self.paciente

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'tb_turnos'
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'
        ordering = ['id']


class Arhivos(models.Model):
    fecha=models.DateField(default=datetime.now, verbose_name='Fecha', null=True, blank=True)
    titulo=models.CharField(max_length=100, verbose_name='titulo', null=True, blank=True)
    documento=models.FileField(upload_to="archivos", verbose_name='documento', null=True, blank=True)

    def __str__(self):
        return self.titulo

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'tb_archivos'
        verbose_name = 'Archivo'
        verbose_name_plural = 'Archivos'
        ordering = ['id']


class Foto(models.Model):
    tratamiento=models.CharField(max_length=10000, verbose_name='Tratamiento', null=True, blank=True)
    imagen=models.ImageField(upload_to="imagenes", verbose_name='Imagen', null=True, blank=True)

    def __str__(self):
        return self.tratamiento

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'tb_foto'
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'
        ordering = ['id']

