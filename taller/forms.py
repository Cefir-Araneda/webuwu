from django import forms
from .models import Genero, Atencion

from django.forms import ModelForm

class GeneroForm(ModelForm):
    class Meta:
        model = Genero
        fields = "__all__"

class AtencionForm(ModelForm):
    class Meta:
        model = Atencion
        fields = "__all__"