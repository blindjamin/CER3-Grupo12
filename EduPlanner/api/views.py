from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Evento, Feriado, Notificacion, Revision
from .serializers import EventoSerializer, FreiadoSerializer, NotificacionSerializer, RevisionSerializer
from rest_framework.permissions import IsAuthenticated

# Vista para listar y crear eventos
class EventoListCreateAPIView(APIView):
    def get(self, request):
        eventos = Evento.objects.all()
        serializer = EventoSerializer(eventos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Vista para listar feriados
class FeriadoListAPIView(APIView):
    def get(self, request):
        feriados = Feriado.objects.all()
        serializer = FreiadoSerializer(feriados, many=True)
        permission_classes = [IsAuthenticated]
        return Response(serializer.data)

# Vista para listar notificaciones
class NotificacionListAPIView(APIView):
    def get(self, request):
        notificaciones = Notificacion.objects.all()
        serializer = NotificacionSerializer(notificaciones, many=True)
        return Response(serializer.data)

class CalendarioConsolidadoAPIView(APIView):
    def get(self, request):
        eventos = Evento.objects.all()
        feriados = Feriado.objects.all()
        data = {
            "eventos": EventoSerializer(eventos, many=True).data,
            "feriados": FreiadoSerializer(feriados, many=True).data,
        }
        return Response(data)
    

