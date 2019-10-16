from django.db import models
from django.utils import timezone
#from django.utils.timezone.now

# Create your models here.

class Pedido(models.Model):
    pedido = models.CharField(max_length=128, blank=True,null=True,)
    cliente = models.ForeignKey('administracion.Cliente', on_delete=models.CASCADE,null=True,blank=True)
    fecha_hora = models.DateField(default=timezone.now, editable=True,)

    productos = models.ManyToManyField('administracion.Producto', through='Pedido_detalle')

    def __str__(self):
        return str(self.pedido)

class Pedido_detalle(models.Model):
    pedido = models.ForeignKey(Pedido,on_delete=models.CASCADE,null=False,blank=False)
    producto = models.ForeignKey('administracion.Producto',on_delete=models.CASCADE,null=False,blank=False)
    cantidad = models.SmallIntegerField(blank=True,null=True)
    precio =  models.DecimalField(max_digits=9,decimal_places=2,null=False,blank=False)
    monto = models.DecimalField(max_digits=9,decimal_places=2,null=False,blank=False)
    def __str__(self):
        return str(self.pedido)+' - '+str(self.producto)

class Documento(models.Model):
    numero = models.SmallIntegerField(blank=True,null=True)
    tipo = models.SmallIntegerField(blank=True,null=True)
    cliente = models.ForeignKey('administracion.Cliente',on_delete=models.CASCADE,null=False,blank=False)
    fecha = models.DateField(default=timezone.now,editable=True,)
    total = models.DecimalField(max_digits=9,decimal_places=2,null=False,blank=False)


class Documento_pedido(models.Model):
    documento = models.ForeignKey(Documento,on_delete=models.CASCADE,null=False,blank=False)
    pedido = models.ForeignKey(Pedido,on_delete=models.CASCADE,null=False,blank=False)
