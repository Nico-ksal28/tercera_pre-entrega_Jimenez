from django.contrib import admin

# Register your models here.

from escaladores.models import Nuevo_escalador, nueva_ruta, nuevo_bloque

admin.site.register(Nuevo_escalador)
admin.site.register(nueva_ruta)
admin.site.register(nuevo_bloque)

