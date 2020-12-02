from django.shortcuts import render
from django.http import HttpResponse

from ebill.models import Cliente, Factura, LineaFactura
# Create your views here.

def inicio(request):
    return render(request, 'ebill/inicio.html')


def vista_clientes(request):
    return render(request, 'ebill/listado_clientes.html',{
        'cliente': Cliente.objects.all()
    })

def detalle_cliente(request, id_cliente):
    return render(request, 'ebill/detalle_cliente.html', {
        'dato_cliente': Cliente.objects.get(pk=id_cliente),
        'factura': Factura.objects.filter(cliente=id_cliente),
    })

def vista_factura(request):
    return render(request, 'ebill/listado_facturas.html',{
        'factura': Factura.objects.all()
    })

def detalle_factura(request, id_factura):
    return render(request, 'ebill/cuerpo_factura.html', {
        'factura': Factura.objects.get(pk= id_factura),
        'linea_factura': LineaFactura.objects.filter(factura = id_factura),
    })



   