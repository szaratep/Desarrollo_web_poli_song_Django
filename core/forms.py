from django import forms
from .models import *

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["nombre", "contrasena"]

class CorreoForm(forms.ModelForm):
    class Meta:
        model = Correo
        fields = ["correo"]

class TelefonoForm(forms.ModelForm):
    class Meta:
        model = Telefono
        fields = ["telefono"]