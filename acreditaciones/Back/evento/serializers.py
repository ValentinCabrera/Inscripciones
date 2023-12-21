from evento.models import Evento, Estado

from rest_framework import serializers

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Estado
        fields = '__all__'
class EventoSerializer(serializers.ModelSerializer):
    estado = EstadoSerializer()
    class Meta:
        model = Evento
        #fields = ['id']
        fields = '__all__'


