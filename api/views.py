from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
import requests
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .models import Sede, Ventanilla
from .utils import enviar_correo
from .serializador import SedeSerializer, VentanillaSerializer

class SedeListCreate(generics.ListCreateAPIView):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer

class SedeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer

class ConsultarVentanillaView(APIView):
    def get(self, request, cedula):
        # Convertir cedula a cadena si es necesario
        cedula = str(cedula)
        
        # Buscar las citas por el número de cédula
        citas = Ventanilla.objects.filter(cedula=cedula)
        
        # Agregar mensajes de depuración
        print("Citas encontradas:", citas)
        
        # Preparar los datos que se pasarán al template
        data = {
            'cedula': cedula,
            'citas': citas,
        }
        
        # Renderizar el template y devolver la respuesta
        return render(request, 'estado_cita.html', data)

class VentanillaListCreate(generics.ListCreateAPIView):
    queryset = Ventanilla.objects.all()
    serializer_class = VentanillaSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        parametros = {
            'nombres': instance.nombres,
            'correo': instance.correo,
            'asunto': 'Mensaje de confirmación',
            'mensaje': 'Bienvenido, la Red de Consultorios Jurídicos Gratuitos UNIANDES dentro de las siguientes 24 horas se pondrá en contacto para confirmar la cita solicitada'
        }
        
        try:
            resultado = enviar_correo(
                parametros['correo'],
                parametros['nombres'],
                parametros['asunto'],
                parametros['mensaje']
            )
            
            return Response({'estado': 'ok'}, status=201)
        
        except requests.exceptions.RequestException as e:
            return Response({'estado': 'error', 'msg': 'Error al enviar correo electrónico: {}'.format(str(e))}, status=500)

class VentanillaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ventanilla.objects.all()
    serializer_class = VentanillaSerializer

class CancelarCitaView(View):
    def get(self, request, cita_id):
        # Buscar la cita por su ID
        cita = get_object_or_404(Ventanilla, pk=cita_id)
        
        # Eliminar la cita
        cita.delete()
        
        # Devolver una respuesta JSON indicando que la cita ha sido cancelada
        return JsonResponse({'message': 'ok'})