from django import forms
from .models import Atencion
from django.forms import ModelForm

class AtencionForm(ModelForm):
    class Meta:
        model = Atencion
        fields = ["mecanico","fecha_atencion","modelo","patente","diagnostico","id_mantencion","cantidad","valor"]
        labels =  {'mecanico':'Mecanico','fecha_atencion':'Fecha (año-mes-dia)','modelo':'Modelo',
                  'patente':'Patente','diagnostico':'Diagnostico','id_mantencion':'Tipo de mantencion',
                  'cantidad':'Cantidad','valor':'Valor total'}