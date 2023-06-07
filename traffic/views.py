from django.http import JsonResponse
from rest_framework.decorators import api_view
from . models import *
from rest_framework.permissions import AllowAny
from rest_framework.decorators import authentication_classes, permission_classes


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def addNewTraffic(request):
    A = Admin.objects.get(id=request.data.get('admin_id'))
    T =  Traffic(f_name = request.data.get('firstname'),l_name = request.data.get('lastname'),
                 user_name = request.data.get('username'), p_image=request.data.get('pimage'),
                 email = request.data.get('email'),phone = request.data.get('phone'),admin = A )
    T.save()
    newserial = [{'status':"created"}] 
    return JsonResponse(newserial,safe=False) 

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def registerAccident(request):
    T = Traffic.objects.get(id=request.data.get('traffic_id'))
    a = Accident(city=request.data.get('city'),date=request.data.get('date'),longitude = request.data.get('longitude'),
                        latitude = request.data.get('latitude'), time = request.data.get('time'), road_type =request.data.get('roadType'),
                        vehicle_speed=request.data.get('vehicleSpeed'), traffic_signal=request.data.get('trafficSignal'), road_side_far=request.data.get('roadSidefar'),
                        injured_people_number=request.data.get('injPeoplenumber'),death_number=request.data.get('deathNumber'), cost_estimation=request.data.get('costEstimation'),
                        traffic=T)
    a.save()
    driver = Driver(accident=a,f_name=request.data.get('driverfname'),l_name=request.data.get('driverlname'),age=request.data.get('driverage'),gender=request.data.get('driverGender'),
                    license_number=request.data.get('driverLicenseNumber'),occupation=request.data.get('driverOccupation'),house_number=request.data.get('driverHouseNumber'),subcity=request.data.get('driverSubcity'),
                    woreda=request.data.get('driverWoreda'),kebele=request.data.get('driverKebele'),phone_number=request.data.get('driverPhonenumber'),
                    isdrunk=request.data.get('isDrunk'))
    driver.save()
    plate = PlateNumber(accident=a, code=request.data.get('plateCode'),city=request.data.get('plateCity'),number=request.data.get('plateNumber'))
    plate.save()
    
    inj_persons = request.data.get('injuredPersons')
    for i in inj_persons:
        inj_person = InjuredPeople(accident=a,injurytype=i['injuryType'],f_name=i['firstName'],l_name=i['lastName'],phone=i['phone'])
        inj_person.save()
    inVolved = request.data.get('involvedVehicles')
    for i in inVolved:
        IV = InvolvedVehicle(accident=a, driver_f_name=i['driverFname'],driver_l_name =i['driverLname'],
                             owner_f_name=i['ownerFname'],owner_l_name=i['driverLname'],
                             driver_license_number = i['driverLicencenumber'],driver_phone=i['driverPhone'],
                             owner_phone=i['ownerPhone'])
        IV.save()
        IVplate = InvolvedVehiclePlate(involved_vehicle=IV, code=i['icode'],city=i['icity'],number=i['inumber'])
        IVplate.save()
    newserial = [{'status':"created"}] 
    return JsonResponse(newserial,safe=False) 
    #acc_images = AccidentImages()
    
