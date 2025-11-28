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

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ["nombre", "contrasena"]

class CorreoProveedorForm(forms.ModelForm):
    class Meta:
        model = CorreoProveedor
        fields = ["correo"]

class TelefonoProveedorForm(forms.ModelForm):
    class Meta:
        model = TelefonoProveedor
        fields = ["telefono"]

class DiscoMp3Form(forms.ModelForm):
    canciones = forms.ModelMultipleChoiceField(
        queryset=Cancion.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Canciones del disco"
    )

    class Meta:
        model = DiscoMp3
        fields = ["nombre", "duracion", "tamano", "precio", "inventario", "canciones"]
class CancionForm(forms.ModelForm):
    class Meta:
        model = Cancion
        fields = ['nombre', 'duracion', 'tamano']


class ViniloForm(forms.ModelForm):
    class Meta:
        model = Vinilo
        fields = ['nombre', 'artista', 'anio_salida', 'precio_unitario', 'inventario', 'proveedor']


class ViniloCancionForm(forms.ModelForm):
    class Meta:
        model = ViniloCancion
        fields = ['vinilo', 'cancion']

