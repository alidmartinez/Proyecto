from django.contrib import admin
from aplic.models import *

class UsuarioAdmin(admin.ModelAdmin):
    list_display=('id','Identificacion','RazonSocial','Nombres','Apellidos')
    
admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Kardex)
admin.site.register(Producto)
admin.site.register(Tercero)
admin.site.register(Parametro)
admin.site.register(ValorParametro)