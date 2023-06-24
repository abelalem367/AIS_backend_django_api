from rest_framework import serializers
from .models import *

class traffic_serializer(serializers.ModelSerializer):
    class Meta:
        model = Traffic
        fields = ('f_name','l_name','user_name','p_image','email','phone','admin')

class adminlogin_serializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('f_name','l_name','username','p_image','email','phone')  

class client_serializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
   
class driver_serializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'
             
class platenumber_serializer(serializers.ModelSerializer):
    class Meta:
        model = PlateNumber
        fields = '__all__'

class injuredpeople_serializer(serializers.ModelSerializer):
    class Meta:
        model = InjuredPeople
        fields = '__all__'
class involvedvehicle_serializer(serializers.ModelSerializer):
    class Meta:
        model = InvolvedVehicle
        fields = '__all__'

class accimages_serializer(serializers.ModelSerializer):
    class Meta:
        model = AccidentImages
        fields = '__all__'

class accident_serializer(serializers.ModelSerializer):
    class Meta:
        model = Accident
        fields = '__all__'