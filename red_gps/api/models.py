from django.db import models
from django.utils import timezone

class Ubicacion(models.Model):
    latitud = models.FloatField()
    longitud = models.FloatField()
    fecha_hora = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.latitud}, {self.longitud} - {self.fecha_hora}"
