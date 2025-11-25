from django.db import models

# =====================
# MODELO: USUARIO
# =====================
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Telefono(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="telefonos")
    telefono = models.CharField(max_length=20)

    class Meta:
        ordering = ["telefono"]
        unique_together = ("usuario", "telefono")

    def __str__(self):
        return self.telefono


class Correo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="correos")
    correo = models.CharField(max_length=120)

    class Meta:
        ordering = ["correo"]
        unique_together = ("usuario", "correo")

    def __str__(self):
        return self.correo


# =====================
# MODELO: CANCIÓN
# =====================
class Cancion(models.Model):
    nombre = models.CharField(max_length=100)
    duracion = models.TimeField()
    tamano = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


# =====================
# MODELO: PROVEEDOR
# =====================
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class TelefonoProveedor(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name="telefonos")
    telefono = models.CharField(max_length=20)

    class Meta:
        ordering = ["telefono"]
        unique_together = ("proveedor", "telefono")

    def __str__(self):
        return self.telefono


class CorreoProveedor(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name="correos")
    correo = models.CharField(max_length=120)

    class Meta:
        ordering = ["correo"]
        unique_together = ("proveedor", "correo")

    def __str__(self):
        return self.correo

# =====================
# MODELO: DISCO MP3
# =====================
class DiscoMp3(models.Model):
    nombre = models.CharField(max_length=100)
    duracion = models.TimeField()
    tamano = models.DecimalField(max_digits=10, decimal_places=2)
    precio = models.FloatField()
    inventario = models.IntegerField(default=0)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre

# =====================
# MODELO: VINILO
# =====================
class Vinilo(models.Model):
    nombre = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    anio_salida = models.IntegerField()
    precio_unitario = models.FloatField()
    inventario = models.IntegerField(default=0)

    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.CASCADE,
        related_name="vinilos"
    )

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre} - {self.artista}"

# =====================
# RELACIONES M:M (VINILOS Y MP3 CON CANCIONES)
# =====================
class ViniloCancion(models.Model):
    vinilo = models.ForeignKey(Vinilo, on_delete=models.CASCADE)
    cancion = models.ForeignKey(Cancion, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("vinilo", "cancion"),)


class DiscoMp3Cancion(models.Model):
    disco_mp3 = models.ForeignKey(DiscoMp3, on_delete=models.CASCADE)
    cancion = models.ForeignKey(Cancion, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("disco_mp3", "cancion"),)


# =====================
# MODELO: PEDIDO (POLIMÓRFICO)
# =====================
class Pedido(models.Model):
    ESTADOS = [
        ("pendiente", "Pendiente"),
        ("aceptado", "Aceptado por proveedor"),
        ("rechazado", "Rechazado por proveedor"),
        ("enviado", "Enviado"),
        ("recibido", "Recibido"),
    ]

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.PROTECT,
        related_name="pedidos",
    )

    vinilo = models.ForeignKey(
        Vinilo,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="pedidos",
    )

    mp3 = models.ForeignKey(
        DiscoMp3,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="pedidos",
    )

    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="pedidos_recibidos",
    )

    fecha_pedido = models.DateField()
    medio_pago = models.CharField(max_length=50)
    estado = models.CharField(max_length=20, choices=ESTADOS, default="pendiente")

    # Campos adicionales
    observacion_rechazo = models.TextField(null=True, blank=True)
    fecha_estimado_envio = models.DateField(null=True, blank=True)
    fecha_envio = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["-fecha_pedido"]


# =====================
# MODELO: VALORACIÓN
# =====================
class Valoracion(models.Model):
    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name="valoraciones"
    )
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name="valoraciones"
    )
    descripcion = models.TextField(max_length=300)

    def __str__(self):
        return f"Valoración de {self.usuario.nombre}"


# =====================
# MODELO: RECOPILACIÓN
# =====================
class Recopilacion(models.Model):
    nombre = models.CharField(max_length=100)
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name="recopilaciones"
    )
    publica = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre


class RecopilacionCancion(models.Model):
    recopilacion = models.ForeignKey(
        Recopilacion,
        on_delete=models.CASCADE
    )
    cancion = models.ForeignKey(
        Cancion,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = (("recopilacion", "cancion"),)
