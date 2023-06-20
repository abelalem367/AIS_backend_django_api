from rest_framework import serializers
from .models import *

class traffic_serializer(serializers.ModelSerializer):
    class Meta:
        model = Traffic
        fields = '__all__'

class client_serializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        
class accident_serializer(serializers.ModelSerializer):
    class Meta:
        model = Accident
        fields = '__all__'