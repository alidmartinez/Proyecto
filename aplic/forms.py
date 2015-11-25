from django import forms
from django.forms import ModelForm
from aplic.models import *

class ParametroForm(forms.Form):
    pass

class UsuarioForm(ModelForm): 
   class Meta:
        model=Usuario
        exclude=["Eliminado"]


class TerceroForm(ModelForm): 
   class Meta:
        model=Tercero
        exclude=["eliminado"]


class KardexForm(ModelForm): 
   class Meta:
        model=Kardex
        exclude=["Eliminado"]

class ProductoForm(ModelForm): 
   class Meta:
        model=Producto
        exclude=["Eliminado"]