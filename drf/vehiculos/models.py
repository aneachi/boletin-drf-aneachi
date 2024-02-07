from django.db import models
from django.utils import timezone

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Marcas"



class Vehiculo(models.Model):
    TIPO_VEHICULO = [
        "Coche",
        "Cliclomotor",
        "Motoclicleta"
    ]
    tipoVehiculo = models.CharField(max_length=20, choices=TIPO_VEHICULO)
    chasis = models.PositiveIntegerField(unique=True)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    modelo = models.CharField(max_length=30)
    matricula = models.CharField(max_length=7, unique=True)
    # color
    fechaFabri = models.DateTimeField(default=timezone.now)
    fechaMatri = models.DateTimeField(null=True)
    fechaBaja = models.DateTimeField(null=True)
    suspendido = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.tipoVehiculo}-{self.marca}-{self.modelo}'

    class Meta:
        verbose_name_plural="Vehículos"
