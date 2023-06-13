from rest_framework import serializers
from .models import *

class traffic_serializer(serializers.ModelSerializer):
    class Meta:
        model = Traffic
        fields = '__all__'