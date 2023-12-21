from django.db import models


class Estado(models.Model):
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre


class Evento(models.Model):
    nombre = models.CharField(max_length=240)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name='eventos')

    def __str__(self):
        return self.nombre


class Inscripto(models.Model):
    nombre = models.CharField(max_length=240)
    apellido = models.CharField(max_length=240, blank=False, null=False)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='inscriptos')
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="incriptos")

    def __str__(self):
        return self.nombre, self.apellido, self.evento



class Evento_Inscripto(models.Model):
    inscripto = models.ForeignKey(Inscripto, on_delete=models.PROTECT, related_name='evento_inscriptos')
    evento = models.ForeignKey(Evento, on_delete=models.PROTECT, related_name='evento_inscriptos')
