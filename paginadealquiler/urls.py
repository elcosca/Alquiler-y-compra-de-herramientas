from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.vistainicio),
        url(r'^herramienta/new/$', views.herramienta_new, name='herramienta_new'),
        url(r'^herramienta/edit/(?P<pk>[0-9]+)$', views.herramienta_edit, name='herramienta_edit'),
        url(r'^herramientas/', views.vistaherramientas),
        url(r'^clientes/', views.vistaclientes),
        url(r'^empresas/', views.vistaempresas),
        url(r'^empleados/', views.vistaempleados),
        url(r'^contrato/new/$', views.contrato_new, name='contrato_new'),
        url(r'^contrato/', views.vistacontrato),
        url(r'^proveedor/new/$', views.proveedor_new, name='proveedor_new'),
        url(r'^proveedor/', views.vistaproveedor),
        url(r'^asociados/', views.vistaasociados),
        url(r'^empresa/new/$', views.empresa_new, name='empresa_new'),
        url(r'^empleado/new/$', views.empleado_new, name='empleado_new'),
        url(r'^cliente/new/$', views.cliente_new, name='cliente_new'),
        url(r'^asociado/new/$', views.asociado_new, name='asociado_new'),
    ]
