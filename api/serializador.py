from rest_framework import serializers
from .models import Sede, Ventanilla

class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = '__all__'

class VentanillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ventanilla
        fields = '__all__'