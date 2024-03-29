from django.http import JsonResponse
from rest_framework.decorators import api_view
from . models import *
from rest_framework.permissions import AllowAny
from rest_framework.decorators import authentication_classes, permission_classes
import bcrypt
from . serializer import *
from django.contrib.auth.models import User
from django.contrib.auth import login
import json
from itertools import chain

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def sendEmail(request):
    message = request.data.get('message')
    email = request.data.get('email')
    title = request.data.get('title')
    send_mail(
        title, message, 'settings.EMAIL_HOST_USER',
        [email], fail_silently=False
    )
    newserial = [{'status':"email successfuly sent"}] 
    return JsonResponse(newserial,safe=False) 


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def addAdmin(request):
    if Admin.objects.all().filter(username=request.data.get('username')):
        newserial = [{'status':"fail",'reason':"account with the username already exists"}]
        return JsonResponse(newserial,safe=False)
    else:
        hashed = bcrypt.hashpw(request.data.get('password').encode('utf8'),bcrypt.gensalt())
        A =  Admin(f_name = request.data.get('firstname'),l_name = request.data.get('lastname'),
                 username = request.data.get('username'),password = hashed.decode('utf8') ,p_image=request.data.get('pimage'),
                 email = request.data.get('email'),phone = request.data.get('phone'))
        A.save()
        u = User.objects.create_user(username=request.data.get('username'),
                                     password=request.data.get('password'),
                                     is_active=True,is_staff=False)
        u.save()
        newserial = [{'status':"created"}] 
        return JsonResponse(newserial,safe=False) 


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def addNewTraffic(request):
    A = Admin.objects.get(id=request.data.get('admin_id'))
    if Traffic.objects.all().filter(user_name=request.data.get('username')):
        newserial = [{'status':"fail",'reason':"account with the username already exists"}]
        return JsonResponse(newserial,safe=False)
    else:
        hashed = bcrypt.hashpw(request.data.get('password').encode('utf8'),bcrypt.gensalt())
        T =  Traffic(f_name = request.data.get('firstname'),l_name = request.data.get('lastname'),
                 user_name = request.data.get('username'),password = hashed.decode('utf8') ,p_image=request.data.get('pimage'),
                 email = request.data.get('email'),phone = request.data.get('phone'),admin = A )
        T.save()
        u = User.objects.create_user(username=request.data.get('username'),
                                     password=request.data.get('password'),
                                     is_active=True,is_staff=False)
        u.save()
        newserial = [{'status':"created"}] 
        return JsonResponse(newserial,safe=False) 



@api_view(['POST']) 
def Login(request):
    usr = request.data.get("username")
    pw = request.data.get("password").encode("utf8")
    adminaccount = Admin.objects.all().filter(username=usr)
    trafficaccount = Traffic.objects.all().filter(user_name=usr)
    clientaccount = Client.objects.all().filter(username=usr)
    if adminaccount:
        serializer = adminlogin_serializer(adminaccount,many=True)
        newserial = list(serializer.data)
        for a in adminaccount:
            if bcrypt.checkpw(pw,a.password.encode('utf-8')):
                if serializer.is_valid:
                    
                    newserial[0]['status']="pass"
                    newserial[0]['accounttype']="admin"
                    newserial[0]['adminID']=a.id            
                    return JsonResponse(newserial, safe=False)
            
            else:
                s = {'status': "fail",'reason':"wrong password"} 
                newserial = [] 
                newserial.append(s) 
                return JsonResponse(newserial,safe=False)
    elif trafficaccount:
        serializer = traffic_serializer(trafficaccount,many=True)
        newserial = list(serializer.data)
        for e in trafficaccount:
            if bcrypt.checkpw(pw,e.password.encode('utf-8')):
                if serializer.is_valid:
                    newserial[0]['status']="pass"
                    newserial[0]['accounttype']="traffic"  
                    newserial[0]['trafficID']=e.id                        
                    return JsonResponse(newserial, safe=False)
            
            else:
                s = {'status': "fail",'reason':"wrong password"} 
                newserial = [] 
                newserial.append(s) 
                return JsonResponse(newserial,safe=False)
    elif clientaccount:
        serializer = client_serializer(clientaccount,many=True)
        newserial = list(serializer.data)
        for p in clientaccount:
            if bcrypt.checkpw(pw,p.password.encode('utf-8')):
                if serializer.is_valid:
                    newserial[0]['status']="pass"
                    newserial[0]['accounttype']="client"    
                    newserial[0]['adminID']=p.id                      
                    return JsonResponse(newserial, safe=False)
            
            else:
                s = {'status': "fail",'reason':"wrong password"} 
                newserial = [] 
                newserial.append(s) 
                return JsonResponse(newserial,safe=False)
    else:
        s = {'status': "fail",'reason':"username doesnot exist"} 
        newserial = [] 
        newserial.append(s) 
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
                             owner_f_name=i['ownerFname'],owner_l_name=i['ownerLname'],
                             driver_license_number = i['driverLicencenumber'],driver_phone=i['driverPhone'],
                             owner_phone=i['ownerPhone'])
        IV.save()
        IVplate = InvolvedVehiclePlate(involved_vehicle=IV, code=i['icode'],city=i['icity'],number=i['inumber'])
        IVplate.save()
    acc_images = request.data.get('images')
    for acc in acc_images:
        print(acc)
        acc_image = AccidentImages(accident=a,image_path=acc)
        acc_image.save()
    newserial = [{'status':"created"}] 
    return JsonResponse(newserial,safe=False) 
    
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def accountcreate(request):
    a = Admin.objects.get(id=request.data.get('admin'))
    
    if Client.objects.all().filter(username=request.data.get('username')):
        newserial = [{'status':"fail",'reason':"account with the username already exists"}]
        return JsonResponse(newserial,safe=False)
    else:
        hashed = bcrypt.hashpw(request.data.get('password').encode('utf8'),bcrypt.gensalt())
        c = Client(name=request.data.get('name'),email=request.data.get('email'),username=request.data.get('username'),
               subcity=request.data.get('subcity'),woreda=request.data.get('woreda'),housenumber=request.data.get('housenumber'),
               kebele=request.data.get('kebele'),phone=request.data.get('phone'),public_key=request.data.get('publickey'),
               private_key=request.data.get('privatekey'),password=hashed.decode('utf8'),isappoved=request.data.get('isapproved'),
               admin=a)
        c.save()
        u = User.objects.create_user(username=request.data.get('username'),
                                     password=request.data.get('password'),
                                     is_active=True,is_staff=False)
        u.save()
        newserial = [{'status':"created"}] 
        return JsonResponse(newserial,safe=False)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def getTraffics(request):
    T = Traffic.objects.all()
    serializer = traffic_serializer(T, many=True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def getClients(request):
    C = Client.objects.all()
    serializer = client_serializer(C, many=True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def getAccidents(request):
    A = Accident.objects.all()
    D = Driver.objects.all()
    P = PlateNumber.objects.all()
    injp = InjuredPeople.objects.all()
    involvedveh = InvolvedVehicle.objects.all()
    acima = AccidentImages.objects.all()
    
    serializer1 = accident_serializer(A, many=True)
    serializer2 = driver_serializer(D, many=True)
    serializer3 = platenumber_serializer(P, many=True)
    serializer4 = injuredpeople_serializer(injp,  many = True)
    serializer5 = involvedvehicle_serializer(involvedveh, many=True)
    serializer6 = accimages_serializer(acima, many=True)
    concatenated_data = []
    concatenated_data.append(serializer1.data)
    concatenated_data.append(serializer2.data)
    concatenated_data.append(serializer3.data)
    concatenated_data.append(serializer4.data)
    concatenated_data.append(serializer5.data)
    concatenated_data.append(serializer6.data)
    return JsonResponse(concatenated_data,safe=False)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def updateaccount(request):
    usr = request.data.get("username")
    adminaccount = Admin.objects.all().filter(username=usr)
    clientaccount = Client.objects.all().filter(username=usr)
    trafficaccount = Traffic.objects.all().filter(user_name=usr)
    if adminaccount:
        adminaccount = Admin.objects.get(username=usr)
        adminaccount.f_name = request.data.get('f_name')
        adminaccount.l_name = request.data.get('l_name')
        adminaccount.email = request.data.get('email')
        adminaccount.phone = request.data.get('phone')
        adminaccount.save()
    elif clientaccount:
        clientaccount = Client.objects.get(username=usr)
        clientaccount.f_name = request.data.get('f_name')
        clientaccount.l_name = request.data.get('l_name')
        clientaccount.email = request.data.get('email')
        clientaccount.phone = request.data.get('phone')
        clientaccount.save()
    elif trafficaccount:
        trafficaccount = Traffic.objects.get(user_name=usr)
        trafficaccount.f_name = request.data.get('f_name')
        trafficaccount.l_name = request.data.get('l_name')
        trafficaccount.save()
    else:
        newserial = [{'status':"fail",'reason':"no account with the provided username exists"}] 
        return JsonResponse(newserial,safe=False)
    newserial = [{'status':"updated successfuly"}] 
    return JsonResponse(newserial,safe=False)
    



@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def changePassword(request):
    typeid = request.data.get('typeid')
    pw = request.data.get('oldpassword').encode('utf8')
    newpw = request.data.get('newpassword').encode('utf8')
    adminaccount = Admin.objects.all().filter(username=typeid)
    trafficaccount = Traffic.objects.all().filter(user_name=typeid)
    clientaccount = Client.objects.all().filter(username=typeid)
    passwordchecker= 'password does not match'
    if adminaccount:
        for a in adminaccount:
            if bcrypt.checkpw(pw,a.password.encode('utf-8')):
                passwordchecker='password matches'
                hashed = bcrypt.hashpw(newpw,bcrypt.gensalt())
                myadminobject = Admin.objects.get(username = typeid)
                u = User.objects.get(username = typeid)
                if u:
                    u.set_password(newpw.decode('utf8'))
                    u.save()
                myadminobject.password = hashed.decode('utf8')
                myadminobject.save()
        if passwordchecker=='password does not match':
            passwordchecker = 'wrong old password'
            
        
    elif trafficaccount:
        for t in trafficaccount:
            if bcrypt.checkpw(pw,t.password.encode('utf-8')):
                passwordchecker='password matches'
                hashed = bcrypt.hashpw(newpw,bcrypt.gensalt())
                mytrafficobject = Traffic.objects.get(user_name = typeid)
                u = User.objects.get(username = typeid)
                if u:
                    u.set_password(newpw.decode('utf8'))
                    u.save()
                mytrafficobject.password = hashed.decode('utf8')
                mytrafficobject.save()
        if passwordchecker=='password does not match':
            passwordchecker = 'wrong old password'

        
    elif clientaccount:
        for c in trafficaccount:
            if bcrypt.checkpw(pw,c.password.encode('utf-8')):
                passwordchecker='password matches'
                hashed = bcrypt.hashpw(newpw,bcrypt.gensalt())
                myclientobject = Client.objects.get(username = typeid)
                u = User.objects.get(username = typeid)
                if u:
                    u.set_password(newpw.decode('utf8'))
                    u.save()
                myclientobject.password = hashed.decode('utf8')
                myclientobject.save()
        if passwordchecker=='password does not match':
            passwordchecker = 'wrong old password'
    else:
        newserial = [{'status':"username not found"}]

    if request.data.get('oldpassword') == request.data.get('newpassword'):
        passwordchecker = 'old and new password are same'
        
    if passwordchecker == 'password matches':
        newserial = [{'status':"password changed successfuly"}] 
    elif passwordchecker == 'wrong old password':
        newserial = [{'status':"wrong old password"}] 
    elif passwordchecker == 'old and new password are same':
        newserial = [{'status':"old and new password are same"}]
    return JsonResponse(newserial,safe=False)

