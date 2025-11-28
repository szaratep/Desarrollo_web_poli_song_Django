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
    canciones = forms.ModelMultipleChoiceField(
        queryset=Cancion.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Canciones del vinilo"
    )
    class Meta:
        model = Vinilo
        fields = ["nombre","artista","anio_salida","precio_unitario","inventario","proveedor","canciones"]

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
            "usuario",
            "vinilo",
            "mp3",
            "proveedor",
            "fecha_pedido",
            "medio_pago",
            "estado",
            "observacion_rechazo",
            "fecha_estimado_envio",
            "fecha_envio",
        ]
        help_texts = {
            "fecha_pedido": "Formato: AAAA-MM-DD (ej: 2025-12-12)",
            "fecha_estimado_envio": "Formato: AAAA-MM-DD (ej: 2025-12-18)",
            "fecha_envio": "Formato: AAAA-MM-DD (ej: 2025-12-17)",
        }
