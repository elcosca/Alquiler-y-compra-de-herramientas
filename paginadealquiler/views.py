from django.shortcuts import render
from .models import Herramientas
from .models import Clientes
from .models import Empresas
from .models import Empleados
from .models import Contrato_de_alquilacion_compra
from .models import Proveedor
from .models import Asociados


def vistainicio(request):
    herramientas = Herramientas.objects.all()
    return render(request, 'inicio.html', {'herramientas': herramientas})


def vistaherramientas(request):
    herramientas = Herramientas.objects.all()
    return render(request, 'herramientas.html', {'herramientas': herramientas})


def vistaclientes(request):
    clientes = Clientes.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})


def vistaempresas(request):
    empresas = Empresas.objects.all()
    return render(request, 'empresas.html', {'empresas': empresas})


def vistaempleados(request):
    empleados = Empleados.objects.all()
    return render(request, 'empleados.html', {'empleados': empleados})


def vistacontrato(request):
    contrato = Contrato_de_alquilacion_compra.objects.all()
    return render(request, 'contrato.html', {'contrato': contrato})


def vistaproveedor(request):
    proveedor = Proveedor.objects.all()
    return render(request, 'proveedor.html', {'proveedor': proveedor})


def vistaasociados(request):
    asociados = Asociados.objects.all()
    return render(request, 'asociados.html', {'asociados': asociados})