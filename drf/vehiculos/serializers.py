from .models import Marca, Vehiculo
from rest_framework import serializers

class MarcaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marca
        fields = ['id', 'nombre', 'url']


class VehiculoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['id', 'chasis', 'marca', 'modelo', 'tipoVehiculo', 'matricula', 'colo', 'fechaFabri', 'fechaMatri', 'fechaBaja','suspendido']