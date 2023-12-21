from django.contrib import admin

# Register your models here.
from .models import Evento, Inscripto, Estado

admin.site.register(Evento)

admin.site.register(Estado)

admin.site.register(Inscripto)