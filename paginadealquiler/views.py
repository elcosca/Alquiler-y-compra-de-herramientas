from django.shortcuts import render
from .models import Herramientas
from .models import Clientes
from .models import Empresas
from .models import Empleados
from .models import Contrato_de_alquilacion_compra
from .models import Proveedor
from .models import Asociados
from .forms import HerramientaForm
from .forms import ProveedorForm
from .forms import EmpresaForm
from .forms import EmpleadoForm
from .forms import ContratoForm
from .forms import ClienteForm
from .forms import AsociadoForm


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


def herramienta_new(request):
        form = HerramientaForm()
        return render(request, 'paginadealquiler/templates/herramientas.html', {'form': form})


def proveedor_new(request):
        form = ProveedorForm()
        return render(request, 'paginadealquiler/proveedor.html', {'form': form})


def empresa_new(request):
        form = EmpresaForm()
        return render(request, 'paginadealquiler/empresas.html', {'form': form})


def empleado_new(request):
        form = EmpleadoForm()
        return render(request, 'paginadealquiler/empleados.html', {'form': form})


def contrato_new(request):
        form = ContratoForm()
        return render(request, 'paginadealquiler/contrato.html', {'form': form})


def cliente_new(request):
        form = ClienteForm()
        return render(request, 'paginadealquiler/clientes.html', {'form': form})


def asociado_new(request):
        form = AsociadoForm()
        return render(request, 'paginadealquiler/asociados.html', {'form': form})
