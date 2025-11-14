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


# =====================
# MODELO: TELEFONO USUARIO
# =====================
class Telefono(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="telefonos")
    telefono = models.CharField(max_length=20, primary_key=True)

    class Meta:
        ordering = ["telefono"]

    def __str__(self):
        return self.telefono


# =====================
# MODELO: CORREO USUARIO
# =====================
class Correo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="correos")
    correo = models.CharField(max_length=120, primary_key=True)

    class Meta:
        ordering = ["correo"]

    def __str__(self):
        return self.correo


# =====================
# MODELO: ITEM
# =====================
class Item(models.Model):
    tipo_item = models.CharField(max_length=50)
    cantidad = models.IntegerField()

    class Meta:
        ordering = ["tipo_item"]

    def __str__(self):
        return f"{self.tipo_item} ({self.cantidad})"


# =====================
# MODELO: PEDIDO
# =====================
class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="pedidos")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="pedidos")
    fecha_pedido = models.DateField()
    estado = models.CharField(max_length=50)
    medio_pago = models.CharField(max_length=50)

    class Meta:
        ordering = ["-fecha_pedido"]

    def __str__(self):
        return f"Pedido {self.id} - {self.usuario.nombre}"


# =====================
# MODELO: VALORACIÓN
# =====================
class Valoracion(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="valoraciones")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="valoraciones")
    descripcion = models.TextField(max_length=300)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"Valoración de {self.usuario.nombre}"


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
    cancion = models.ForeignKey(Cancion, on_delete=models.CASCADE, related_name="vinilos")
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name="vinilos")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="vinilos")

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre} - {self.artista}"


# =====================
# MODELO: DISCO MP3
# =====================
class DiscoMp3(models.Model):
    nombre = models.CharField(max_length=100)
    duracion = models.TimeField()
    tamano = models.DecimalField(max_digits=10, decimal_places=2)
    precio = models.FloatField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="discos_mp3")

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


# =====================
# MODELO: RELACIONES MUCHOS A MUCHOS
# =====================
class ViniloCancion(models.Model):
    vinilo = models.ForeignKey(Vinilo, on_delete=models.CASCADE)
    cancion = models.ForeignKey(Cancion, on_delete=models.CASCADE)

    class Meta:
        unique_together = [("vinilo", "cancion")]


class DiscoMp3Cancion(models.Model):
    disco_mp3 = models.ForeignKey(DiscoMp3, on_delete=models.CASCADE)
    cancion = models.ForeignKey(Cancion, on_delete=models.CASCADE)

    class Meta:
        unique_together = [("disco_mp3", "cancion")]


# =====================
# MODELO: CORREO Y TELÉFONO PROVEEDOR
# =====================
class CorreoProveedor(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name="correos")
    correo = models.CharField(max_length=120, primary_key=True)

    def __str__(self):
        return self.correo


class TelefonoProveedor(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name="telefonos")
    telefono = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.telefono


# =====================
# MODELO: RECOPILACIÓN
# =====================
class Recopilacion(models.Model):
    nombre = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="recopilaciones")
    publica = models.BooleanField(default=False)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class RecopilacionCancion(models.Model):
    recopilacion = models.ForeignKey(Recopilacion, on_delete=models.CASCADE)
    cancion = models.ForeignKey(Cancion, on_delete=models.CASCADE)

    class Meta:
        unique_together = [("recopilacion", "cancion")]
