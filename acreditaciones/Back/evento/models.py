

from django.db import models
from django.db.models import ForeignKey

class TipoEstado(models.Model):
    nombre = models.CharField(max_length=80)


class Estado(models.Model):
    nombre = models.CharField(max_length=80)
    tipoEstado = models.ForeignKey(TipoEstado, on_delete=models.CASCADE, related_name='estados')

    def __str__(self):
        return self.nombre


class Grupo(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

class Pais(models.Model):
    nombre = models.CharField(max_length=150)


class Provincia(models.Model):
    nombre = models.CharField(max_length=150)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT, related_name='provincias')


class Localidad(models.Model):
    nombre = models.CharField(max_length=150)
    provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT, related_name='localidades')
    codigoPostal = models.IntegerField()


class Ubicacion(models.Model):
    localidad = models.ForeignKey(Localidad, on_delete=models.PROTECT, related_name='ubicaciones')
    calle =models.CharField(max_length=150)
    nro =models.IntegerField()
    coordenada =models.CharField(max_length=80, blank=True, null=False)

class Evento(models.Model):
    nombre = models.CharField(max_length=240)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name='eventos')
    fechaHora = models.DateTimeField(auto_now=True)
    ubicacion = ForeignKey(Ubicacion, on_delete=models.CASCADE, related_name='eventos')

    def __str__(self):
        return self.nombre

class DetalleEvento(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='detalle')
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='detalle')


class Inscripto(models.Model):
    nombre = models.CharField(max_length=240)
    apellido = models.CharField(max_length=240, blank=False, null=False)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='inscriptos')
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="incriptos")

    def __str__(self):
        return self.nombre, self.apellido, self.evento


class DetalleInscripto(models.Model):
    inscripto = models.ForeignKey(Inscripto, on_delete=models.CASCADE, related_name='detalleInscriptos')
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='detalleInscriptos')


class Pago(models.Model):
    total = models.DecimalField(max_digits=16,
        decimal_places=2,
        null=True,
        blank=True)
    fecha = models.DateTimeField(auto_now=True)
    pagado = models.BooleanField()


class HistorialPrecio(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='historialPrecios')
    precio = models.DecimalField(max_digits=16,
                                 decimal_places=2,
                                 null=True,
                                 blank=True)
    fechaHora = models.DateTimeField(auto_now=True)



class Inscripcion(models.Model):
    inscripto = models.ForeignKey(Inscripto, on_delete=models.PROTECT, related_name='inscripcion')
    evento = models.ForeignKey(Evento, on_delete=models.PROTECT, related_name='inscripcion')
    fechaHora = models.DateTimeField(auto_now=True)
    pago = models.ForeignKey(Pago, on_delete=models.PROTECT, related_name='inscripcion')
    qr = models.CharField(max_length=80, blank=False, null=False, unique=True)



class Checkin(models.Model):
    fechaHora = models.DateTimeField(auto_now=True)
    inscripto = models.ForeignKey(Inscripto, on_delete=models.CASCADE, related_name='checkins')
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name='checkins')




