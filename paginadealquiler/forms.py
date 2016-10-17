from django import forms
from .models import Herramientas
from .models import Proveedor
from .models import Empresas
from .models import Empleados
from .models import Contrato_de_alquilacion_compra
from .models import Clientes
from .models import Asociados


class HerramientaForm(forms.ModelForm):

        class Meta:
            model = Herramientas
            fields = ('nombre_de_la_herramienta', 'precio',)


class ProveedorForm(forms.ModelForm):

        class Meta:
            model = Proveedor
            fields = ('nombre_del_proveedor', 'direccion_de_correo',)


class EmpresaForm(forms.ModelForm):

        class Meta:
            model = Empresas
            fields = ('nombre', 'direccion_de_correo',)


class EmpleadoForm(forms.ModelForm):

        class Meta:
            model = Empleados
            fields = ('nombre', 'direccion_de_correo',)


class ContratoForm(forms.ModelForm):

        class Meta:
            model = Contrato_de_alquilacion_compra
            fields = ('id_contrato', 'proposito',)


class ClienteForm(forms.ModelForm):

        class Meta:
            model = Clientes
            fields = ('nombre', 'direccion_de_correo',)


class AsociadoForm(forms.ModelForm):

        class Meta:
            model = Asociados
            fields = ('id_asociado',)

