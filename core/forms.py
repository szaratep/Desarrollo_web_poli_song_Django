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

class ValoracionForm(forms.ModelForm):
    class Meta:
        model = Valoracion
        fields = ["pedido", "usuario", "descripcion"]

class RecopilacionForm(forms.ModelForm):
    class Meta:
        model = Recopilacion
        fields = ["nombre", "usuario", "publica"]

class RecopilacionCancionForm(forms.ModelForm):
    class Meta:
        model = RecopilacionCancion
        fields = ["recopilacion", "cancion"]