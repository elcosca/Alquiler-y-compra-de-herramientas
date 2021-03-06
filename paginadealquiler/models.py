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
    turno = models.CharField(max_length=200)

    def __str__(self):
        return self.turno


class Contrato_de_alquilacion_compra(models.Model):
    id_contrato = models.IntegerField()
    nombre_del_cliente = models.ForeignKey('Clientes')
    nombre_de_la_empresa = models.ForeignKey('Empresas')
    horario_de_alquiler_compra = models.DateTimeField(default=timezone.now)
    empleado = models.ForeignKey('Empleados')
    proposito = models.CharField(max_length=200)
    herramienta = models.ForeignKey('Herramientas')
    cantidad = models.IntegerField()
    fecha_de_entrega = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.proposito


class Proveedor(models.Model):
    id_proveedor = models.IntegerField()
    nombre_del_proveedor = models.CharField(max_length=200)
    direccion_de_correo = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_del_proveedor


class Asociados(models.Model):
    id_asociado = models.CharField(max_length=200)
    cliente = models.ForeignKey('Clientes')
    empresa = models.ForeignKey('Empresas')
    beneficio = models.ForeignKey('Beneficio')
    renovar_asociacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.id_asociado


class Beneficio(models.Model):
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion


class Comprar(models.Model):
    id_compra = models.CharField(max_length=200)
    cliente = models.ForeignKey('Clientes')
    empleado = models.ForeignKey('Empleados')
    herramienta = models.ForeignKey('Herramientas')
    cantidad = models.IntegerField()
    total = models.CharField(max_length=200)

    def __str__(self):
        return self.id_compra


class Alquiler(models.Model):
    id_alquiler = models.CharField(max_length=200)
    cliente = models.ForeignKey('Clientes')
    empleado = models.ForeignKey('Empleados')
    herramienta = models.ForeignKey('Herramientas')
    cantidad = models.IntegerField()
    total = models.CharField(max_length=200)
    fecha_de_entrega = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.id_alquiler