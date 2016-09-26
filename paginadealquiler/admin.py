from django.contrib import admin
from .models import Clientes
from .models import Empleados
from .models import Herramientas
from .models import Empresas
from .models import Asociados
from .models import Proveedor
from .models import Contrato_de_alquilacion_compra
from .models import Turnos
from .models import Beneficio


admin.site.register(Clientes)
admin.site.register(Empleados)
admin.site.register(Herramientas)
admin.site.register(Empresas)
admin.site.register(Asociados)
admin.site.register(Proveedor)
admin.site.register(Contrato_de_alquilacion_compra)
admin.site.register(Turnos)
admin.site.register(Beneficio)


