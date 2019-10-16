from django.db import models

# Create your models here.

class Ciudad(models.Model):
    ciudad = models.CharField(max_length=128, blank=True,null=True,unique=True)
    def __str__(self):
        return str(self.ciudad)

class Comuna(models.Model):
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    comuna = models.CharField(max_length=128, blank=True,null=True,unique=True)
    def __str__(self):
        return str(self.comuna)

class Condicion_de_pago(models.Model):
    condicion_de_pago = models.CharField(max_length=128, blank=True,null=True,unique=True)
    dias = models.SmallIntegerField(blank=True,null=True,unique=True)
    def __str__(self):
        return str(self.condicion_de_pago)

class Familia_producto(models.Model):
    familia = models.CharField(max_length=128,blank=False,null=False,unique=True)
    def __str__(self):
        return str(self.familia)

class Producto(models.Model):
    familia_producto = models.ForeignKey(Familia_producto, on_delete=models.CASCADE,null=True,blank=True)
    producto = models.CharField(max_length=128,null=False,blank=False,unique=True)
    def __str__(self):
        return str(self.producto)

class Cliente(models.Model):
    rut = models.CharField(max_length=11, blank=True,null=True,unique=True)
    razon_social = models.CharField(max_length=128, blank=True, null=True, unique=True)
    nombre = models.CharField(max_length=128, blank=True,null=True,unique=True)
    direccion = models.CharField(max_length=100, blank=True, null=True, )
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE,null=True,blank=True)
    giro = models.CharField(max_length=128, blank=True,null=True,)
    telefono = models.CharField(max_length=16, blank=True,null=True,)
    correo_electronico = models.CharField(max_length=64, blank=True,null=True,)
    condicion_de_pago = models.ForeignKey(Condicion_de_pago, on_delete=models.CASCADE,null=True,blank=True)

    precios = models.ManyToManyField(Producto, through='Precio')

    def __str__(self):
        return str(self.nombre)

class Precio(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE,null=True,blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,null=True,blank=True)
    precio = models.DecimalField(max_digits=9,decimal_places=2,null=False,blank=False)

    def __str__(self):
        return str(self.cliente) + ' - ' + str(self.producto) + ' - ' + str(self.precio)

