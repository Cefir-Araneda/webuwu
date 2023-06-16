from django.contrib import admin
from .models import Mecanico, Genero, Mantencion, Atencion

# Register your models here.
admin.site.register(Mecanico)
admin.site.register(Genero)
admin.site.register(Mantencion)
admin.site.register(Atencion)
