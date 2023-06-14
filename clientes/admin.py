from django.contrib import admin
from .models import Genero, Mecanico, Mantencion ,Atencion 

# Register your models here.
admin.site.register(Genero)
admin.site.register(Mecanico)
admin.site.register(Mantencion)
admin.site.register(Atencion)