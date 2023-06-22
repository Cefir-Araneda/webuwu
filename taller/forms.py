from django import forms
from .models import Atencion
from django.forms import ModelForm

class AtencionForm(ModelForm):
    class Meta:
        model = Atencion
        fields = '__all__'