from django.db import models

# Create your models here.
class Cliente(models.Model):
    nif = models.CharField(max_length=8, primary_key=True)
    nombre = models.CharField(max_length=12)
    apellidos = models.CharField(max_length=30)
    direccion = models.CharField(max_length=100)
    empresa = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f'{self.empresa}'

class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    anio = models.DateTimeField(auto_now_add=True, verbose_name='Año',)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,  
    )
#En este caso uso on_delete = models.PROTECT para evitar el borrado accidental.
#Asi nos aseguramos de saber que estamos borrando las facturas antes de eliminar el Cliente.
    def __str__(self):
        return f'Factura: {self.id_factura} - {self.cliente.empresa}'


class LineaFactura(models.Model):
    producto_nombre = models.CharField(max_length=50)
    precio_unitario = models.FloatField()
    unidades = models.IntegerField()
    factura = models.ForeignKey(
        Factura,
        on_delete=models.CASCADE,
    )
#He aplicado on_delete = models.CASCADE, porque entiendo que no tiene sentido tener que eliminar una a una
#cada linea de una factura antes de poder eliminar la factura en sí misma.
    def precio_real(self):
        return (self.precio_unitario * self.unidades)




