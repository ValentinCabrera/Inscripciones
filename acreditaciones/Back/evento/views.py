
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from evento.models import Evento
from evento.serializers import EventoSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class ListarEventos(APIView):

    def get(self, request):
        eventos = Evento.objects.all()
        serializer = EventoSerializer(eventos, many=True)

        # Puedes usar JsonResponse para devolver una respuesta JSON
        #data = {'eventos': list(eventos.values())}

        return Response(serializer.data)

