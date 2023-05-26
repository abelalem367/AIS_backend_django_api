from rest_framework import serializers
from .models import *

class ais_serializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class adminlogin_serializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('f_name','l_name','username','p_image','email','phone')    

class expertlogin_serializer(serializers.ModelSerializer):
    class Meta:
        model = Expert
        fields = ('f_name','l_name','username','p_image','email','phone','admin_id')
    
        
class garagelogin_serializer(serializers.ModelSerializer):
    class Meta:
        model = Garage
        fields = ('name','username','address','email','phone')
class proposerlogin_serializer(serializers.ModelSerializer):
    class Meta:
        model = Proposer
        fields = ('f_name','l_name','username','p_image')