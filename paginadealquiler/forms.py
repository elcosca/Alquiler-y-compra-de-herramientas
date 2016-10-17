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
            fields = ('nombre_de_la_herramienta', 'precio', 'id_herramienta', 'stock')


class ProveedorForm(forms.ModelForm):

        class Meta:
            model = Proveedor
            fields = ('nombre_del_proveedor', 'direccion_de_correo', 'id_proveedor', 'telefono')


class EmpresaForm(forms.ModelForm):

        class Meta:
            model = Empresas
            fields = ('nombre', 'direccion_de_correo', 'id_empresas', 'domilicio', 'telefono', 'herramientas_que_posee')


class EmpleadoForm(forms.ModelForm):

        class Meta:
            model = Empleados
            fields = ('nombre', 'direccion_de_correo', 'id_empleados', 'apellido', 'DNI', 'fecha_de_nacimiento', 'numero_de_empleado', 'telefono', 'domicilio', 'turnos')


class ContratoForm(forms.ModelForm):

        class Meta:
            model = Contrato_de_alquilacion_compra
            fields = ('id_contrato', 'proposito', 'nombre_del_cliente', 'nombre_de_la_empresa', 'horario_de_alquiler_compra', 'empleado', 'herramienta', 'cantidad', 'fecha_de_entrega')


class ClienteForm(forms.ModelForm):

        class Meta:
            model = Clientes
            fields = ('nombre', 'direccion_de_correo', 'id_cliente', 'apellido', 'dni', 'domilicio', 'telefono', 'fecha_de_nacimiento', 'herramienta_que_posee')


class AsociadoForm(forms.ModelForm):

        class Meta:
            model = Asociados
            fields = ('id_asociado', 'cliente', 'empresa', 'beneficio', 'renovar_asociacion')


