from django.db import models
from django.utils import timezone


class Herramientas (models.Model):
    nombre_de_la_herramienta = models.CharField(max_length=200)
    id_herramienta = models.IntegerField()
    precio = models.CharField(max_length=200)
    stock = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_de_la_herramienta


class Clientes (models.Model):
    id_cliente = models.IntegerField()
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.IntegerField()
    direccion_de_correo = models.CharField(max_length=200)
    domilicio = models.CharField(max_length=200)
    telefono = models.IntegerField()
    fecha_de_nacimiento = models.DateTimeField(default=timezone.now)
    herramienta_que_posee = models.ForeignKey('Herramientas')

    def __str__(self):
        return self.apellido


class Empresas (models.Model):
    id_empresas = models.IntegerField()
    nombre = models.CharField(max_length=200)
    direccion_de_correo = models.CharField(max_length=200)
    domilicio = models.CharField(max_length=200)
    telefono = models.IntegerField()
    herramientas_que_posee = models.ForeignKey('Herramientas')

    def __str__(self):
        return self.nombre


class Empleados (models.Model):
    id_empleados = models.IntegerField()
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    DNI = models.IntegerField()
    direccion_de_correo = models.CharField(max_length=200)
    fecha_de_nacimiento = models.DateTimeField(default=timezone.now)
    numero_de_empleado = models.IntegerField()
    telefono = models.CharField(max_length=200)
    domicilio = models.CharField(max_length=200)
    turnos = models.ForeignKey('Turnos')

    def __str__(self):
        return self.apellido


class Turnos(models.Model):
    id_turno = models.IntegerField()
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Contrato_de_alquilacion_compra(models.Model):
    id_contrato = models.IntegerField()
    nombre_del_cliente = models.ForeignKey('Clientes')
    nombre_de_la_empresa = models.ForeignKey('Empresas')
    horario_de_alquiler_compra = models.DateTimeField(default=timezone.now)
    empleado = models.ForeignKey('Empleados')
    objetivo = models.CharField(max_length=200)
    herramienta = models.ForeignKey('Herramientas')
    cantidad = models.IntegerField()
    fecha_de_entrega = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.horario_de_alquiler


class Proveedor(models.Model):
    id_proveedor = models.IntegerField()
    nombre_del_proveedor = models.CharField(max_length=200)
    direccion_de_correo = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_del_proveedor


class Asociados(models.Model):
    numero_de_asociado = models.CharField(max_length=200)
    id_asociado = models.IntegerField()
    cliente = models.ForeignKey('Clientes')
    empresa = models.ForeignKey('Empresas')
    beneficio = models.CharField(max_length=200)
    renovar_asociacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.cliente
