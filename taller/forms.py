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

class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Tu nombre")
    email = forms.EmailField(label="Tu correo electronico")
    asunto = forms.CharField(label="Tu asunto")
    mensaje = forms.CharField(widget=forms.Textarea, label="Tu mensaje")