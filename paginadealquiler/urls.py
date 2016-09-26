from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.vistainicio),
        url(r'^herramientas/', views.vistaherramientas),
        url(r'^clientes/', views.vistaclientes),
        url(r'^empresas/', views.vistaempresas),
        url(r'^empleados/', views.vistaempleados),
        url(r'^contrato/', views.vistacontrato),
        url(r'^proveedor/', views.vistaproveedor),
        url(r'^asociados/', views.vistaasociados),
    ]
