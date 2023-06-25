from rest_framework import serializers
from .models import *

class ais_serializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class vehicle_serializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class previousaccident_serializer(serializers.ModelSerializer):
    class Meta:
        model = PreviousAccident
        fields = ('vehicle','accident_date','vehicle_damage','personal_claims','property_damage')
class otherinsurance_serializer(serializers.ModelSerializer):
    class Meta:
        model = OtherInsurances
        fields = '__all__'
class vehicleplate_serializer(serializers.ModelSerializer):
    class Meta:
        model = VehiclePlate
        fields = '__all__'
class claim_serializer(serializers.ModelSerializer):
    class Meta:
        model = Claim
        fields = '__all__'

class vehiclecontract_serializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleContract
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