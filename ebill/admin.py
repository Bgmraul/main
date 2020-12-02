from django.contrib import admin

# Register your models here.
from ebill.models import Cliente, Factura, LineaFactura

class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'nif',
        'nombre',
        'apellidos',
        'direccion',
        'empresa'
    )
    search_fields = ('nif', 'apellido', 'empresa')
admin.site.register(Cliente, ClienteAdmin)

class FacturaAdmin(admin.ModelAdmin):
    list_display = (
        'id_factura',
        'anio',
        'fecha_emision',
        'cliente',
    )

    search_fields = ('anio', 'fecha_emision', 'cliente')
admin.site.register(Factura, FacturaAdmin)

class LineaFacturaAdmin(admin.ModelAdmin):
    list_display = (
        'producto_nombre',
        'precio_unitario',
        'unidades',
        'factura',
    )
admin.site.register(LineaFactura, LineaFacturaAdmin)