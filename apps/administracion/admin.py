from django.contrib import admin
from django.contrib.admin import AdminSite
from apps.administracion.models import Condicion_de_pago,Comuna,Ciudad,Cliente,Familia_producto,Producto
from apps.administracion.models import Precio
from apps.operacion.models import Pedido,Pedido_detalle,Documento,Documento_pedido

# Register your models here.

class SitioPrincipal(AdminSite):
    site_header = 'Venta movil'
    site_title = 'Aclanados?'
    index_title = "El sistema completo y sus funciones ..."
sitio_principal = SitioPrincipal(name='configuracion')


class Comunas_enlinea(admin.TabularInline):
#class Comunas_enlinea(admin.StackedInline):
    model = Comuna
    extra = 0
class Ciudad_admin(admin.ModelAdmin):
    inlines = [Comunas_enlinea,]

class Productos_enlinea(admin.TabularInline):
#class Productos_enlinea(admin.StackedInline):
    model = Producto
    extra = 0
class Familia_producto_admin(admin.ModelAdmin):
    inlines = [Productos_enlinea,]
# ----------------------------------------------------------------
class Precio_enlinea(admin.TabularInline):
    model = Precio
    extra = 1

class Cliente_admin(admin.ModelAdmin):
    inlines = (Precio_enlinea,)

class Producto_admin(admin.ModelAdmin):
    inlines = (Precio_enlinea,)
# ----------------------------------------------------------------
class Pedido_detalle_enlinea(admin.TabularInline):
    model = Pedido_detalle
    extra = 1

class Pedido_admin(admin.ModelAdmin):
    inlines = (Pedido_detalle_enlinea,)
# ----------------------------------------------------------------
# ----------------------------------------------------------------
class Documento_pedido_enlinea(admin.TabularInline):
    model = Documento_pedido
    extra = 1

class Documento_admin(admin.ModelAdmin):
    inlines = (Documento_pedido_enlinea,)
# ----------------------------------------------------------------

sitio_principal.register(Condicion_de_pago)
sitio_principal.register(Ciudad,Ciudad_admin)
sitio_principal.register(Comuna)
sitio_principal.register(Cliente,Cliente_admin)
sitio_principal.register(Familia_producto,Familia_producto_admin)
sitio_principal.register(Producto,)
sitio_principal.register(Precio)
sitio_principal.register(Pedido,Pedido_admin)
sitio_principal.register(Pedido_detalle)
sitio_principal.register(Documento,Documento_admin)
sitio_principal.register(Documento_pedido)

