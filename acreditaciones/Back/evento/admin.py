from django.contrib import admin

# Register your models here.
from .models import Evento, Inscripto, Estado, DetalleEvento, Grupo, Pais, Provincia, Localidad, Ubicacion, TipoEstado, Checkin, DetalleInscripto, Inscripcion, Pago, HistorialPrecio

admin.site.register(Evento)
admin.site.register(Estado)
admin.site.register(Inscripto)
admin.site.register(TipoEstado)
admin.site.register(Grupo)
admin.site.register(Pais)
admin.site.register(Provincia)
admin.site.register(Localidad)
admin.site.register(Ubicacion)
admin.site.register(HistorialPrecio)
admin.site.register(Checkin)
admin.site.register(DetalleEvento)
admin.site.register(DetalleInscripto)
admin.site.register(Inscripcion)
admin.site.register(Pago)

