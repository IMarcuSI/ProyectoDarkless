from django import forms
from .models import Genero, Usuario, Tipo, Ropa2

from django.forms import ModelForm

class GeneroForm(ModelForm):
    class Meta:
        model = Genero
        fields = "__all__"

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"

class TipoForm(ModelForm):
    class Meta:
        model = Tipo
        fields = "__all__"

class Ropa2Form(ModelForm):
    class Meta:
        model = Ropa2
        fields = "__all__"