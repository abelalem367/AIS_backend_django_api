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
        
class accident_serializer(serializers.ModelSerializer):
    class Meta:
        model = Accident
        fields = '__all__'