from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
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
    if request.method == "POST":
        form = HerramientaForm(request.POST)
    if form.is_valid():
                herramienta = form.save(commit=False)
                herramienta.save()
                return redirect('/')
    else:
            form = HerramientaForm()
    herramientas = Herramientas.objects.all()
    return render(request, 'herramienta-new.html', {'herramientas': herramientas, 'form' : form})

def herramienta_edit(request, pk):
        herramienta = get_object_or_404(Herramientas, pk=pk)
        if request.method == "POST":
            form = HerramientaForm(request.POST, instance=herramienta)
            if form.is_valid():
                herramienta = form.save(commit=False)
                herramienta.save()
                herramientas = Herramientas.objects.all()
                return render(request, 'herramientas.html', {'herramientas': herramientas})
        else:
            form = HerramientaForm(instance=herramienta)
        return render(request, 'herramienta-edit.html', {'form': form})

def herramienta_eliminar (request, pk):
        Herramientas.objects.filter(pk=pk).delete()
        herramientas = Herramientas.objects.all()
        return render(request, 'herramientas.html', {'herramientas': herramientas})


def proveedor_new(request):
    form = ProveedorForm()
    if request.method == "POST":
        form = ProveedorForm(request.POST)
    if form.is_valid():
                proveedor = form.save(commit=False)
                proveedor.save()
                return redirect('/')
    else:
            form = ProveedorForm()
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor-new.html', {'proveedores': proveedores, 'form' : form})

'''
def proveedor_edit(request, pk):
        proveedor = get_object_or_404(Proveedor, pk=pk)
        if request.method == "POST":
            form = ProveedorForm(request.POST, instance=proveedor)
            if form.is_valid():
                proveedor = form.save(commit=False)
                proveedor.save()
                return redirect('/', pk=proveedor.pk)
        else:
            form = ProveedorForm(instance=proveedor)
        return render(request, '/proveedor-edit.html', {'form': form})
'''

def empresa_new(request):
    form = EmpresaForm()
    if request.method == "POST":
        form = EmpresaForm(request.POST)
    if form.is_valid():
                empresa = form.save(commit=False)
                empresa.save()
                return redirect('/')
    else:
            form = EmpresaForm()
    empresas = Empresas.objects.all()
    return render(request, 'empresa-new.html', {'empresas': empresas, 'form' : form})

'''
def empresa_edit(request, pk):
        empresa = get_object_or_404(Herramientas, pk=pk)
        if request.method == "POST":
            form = HerramientaForm(request.POST, instance=herramienta)
            if form.is_valid():
                herramienta = form.save(commit=False)
                herramienta.save()
                return redirect('/', pk=herramienta.pk)
        else:
            form = HerramientaForm(instance=herramienta)
        return render(request, '/herramienta-edit.html', {'form': form})
'''

def empleado_new(request):
    form = EmpleadoForm()
    if request.method == "POST":
        form = EmpleadoForm(request.POST)
    if form.is_valid():
                empleado = form.save(commit=False)
                empleado.save()
                return redirect('/')
    else:
            form = EmpleadoForm()
    empleados = Empleados.objects.all()
    return render(request, 'empleado-new.html', {'empleados': empleados, 'form' : form})


def contrato_new(request):
    form = ContratoForm()
    if request.method == "POST":
        form = ContratoForm(request.POST)
    if form.is_valid():
                contrato = form.save(commit=False)
                contrato.save()
                return redirect('/')
    else:
            form = ContratoForm()
    contratos = Contrato_de_alquilacion_compra.objects.all()
    return render(request, 'contrato-new.html', {'contratos': contratos, 'form' : form})


def cliente_new(request):
    form = ClienteForm()
    if request.method == "POST":
        form = ClienteForm(request.POST)
    if form.is_valid():
                cliente = form.save(commit=False)
                cliente.save()
                return redirect('/')
    else:
            form = ClienteForm()
    clientes = Clientes.objects.all()
    return render(request, 'cliente-new.html', {'clientes': clientes, 'form' : form})


def asociado_new(request):
    form = AsociadoForm()
    if request.method == "POST":
        form = AsociadoForm(request.POST)
    if form.is_valid():
                asociado = form.save(commit=False)
                asociado.save()
                return redirect('/')
    else:
            form = ContratoForm()
    asociados = Asociados.objects.all()
    return render(request, 'asociado-new.html', {'asociados': asociados, 'form' : form})
