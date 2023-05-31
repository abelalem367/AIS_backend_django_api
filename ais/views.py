from rest_framework.decorators import api_view
from . serializer import *
from . models import *
from django.http import JsonResponse
import bcrypt
from django.contrib.auth.models import User
from django.contrib.auth import login
from rest_framework.permissions import AllowAny
from rest_framework.decorators import authentication_classes, permission_classes


@api_view(['GET'])
def getData(request):
    items = Admin.objects.all()
    serializer = ais_serializer(items, many=True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['POST'])
def createVehicleInsurance(request):
    expert = Expert.objects.get(id=request.data.get('expertId'))
    proposer = Proposer.objects.get(id = request.data.get('proposerId'))
    v = Vehicle(
                    engine_number=request.data.get('engineNumber'),chassis_number=request.data.get('chassisNumber'),
                    owner_f_name=request.data.get('firstName'),owner_l_name=request.data.get('lastName'),
                    purpose=request.data.get('purpose'),body_type=request.data.get('bodyType'),
                    horse_power=request.data.get('horsePower'),good_capacity=request.data.get('goodCapacity'),
                    passenger_capacity=request.data.get('passengerCapacity'),bsg_action=request.data.get('bsgAction'),
                    cover_required=request.data.get('coverRequired'),drivers_covered=request.data.get('driversCovered'),
                    expert = expert ,proposer = proposer
                )      
    v.save()
    O = OtherInsurances(
        v.id,cancel = request.data.get('cancel'),decline=request.data.get('decline'),
        iae = request.data.get('iae'),isc = request.data.get('isc'),refuse = request.data.get('refuse'),
        requires = request.data.get('requires')
    )
    O.save()
    E = ExtraFitting(
        v.id,radio = request.data.get('radio'),communication = request.data.get('communication'),
        bsd = request.data.get('bsd')
    )
    E.save()
    p_accident_array = request.data.get('previousAccident')
    
    for x in p_accident_array:
        pa = PreviousAccident(vehicle=v,accident_date = x['accidentDate'],vehicle_damage= x['vechileDamage'],
            personal_claims = x['personalInjury'], property_damage = x['propertyDamage'])
        pa.save()
    newserial = [{'status':"created"}] 
    return JsonResponse(newserial,safe=False) 


@api_view(['POST']) 
def Login(request):
    usr = request.data.get("username")
    pw = request.data.get("password").encode("utf8")
    adminaccount = Admin.objects.all().filter(username=usr)
    expertaccount = Expert.objects.all().filter(username=usr)
    proposeraccount = Proposer.objects.all().filter(username=usr)
    garageaccount = Garage.objects.all().filter(username=usr)
    if adminaccount:
        serializer = adminlogin_serializer(adminaccount,many=True)
        newserial = list(serializer.data)
        for a in adminaccount:
            if bcrypt.checkpw(pw,a.password.encode('utf-8')):
                if serializer.is_valid:
                    
                    newserial[0]['status']="pass"
                    newserial[0]['account type']="admin"            
                    return JsonResponse(newserial, safe=False)
            
            else:
                s = {'status': "fail",'reason':"wrong password"} 
                newserial = [] 
                newserial.append(s) 
                return JsonResponse(newserial,safe=False)
    elif expertaccount:
        serializer = expertlogin_serializer(expertaccount,many=True)
        newserial = list(serializer.data)
        for e in expertaccount:
            if bcrypt.checkpw(pw,e.password.encode('utf-8')):
                if serializer.is_valid:
                    newserial[0]['status']="pass"
                    newserial[0]['account type']="expert"              
                    return JsonResponse(newserial, safe=False)
            
            else:
                s = {'status': "fail",'reason':"wrong password"} 
                newserial = [] 
                newserial.append(s) 
                return JsonResponse(newserial,safe=False)
    elif proposeraccount:
        serializer = proposerlogin_serializer(proposeraccount,many=True)
        newserial = list(serializer.data)
        for p in proposeraccount:
            if bcrypt.checkpw(pw,p.password.encode('utf-8')):
                if serializer.is_valid:
                    newserial[0]['status']="pass"
                    newserial[0]['account type']="proposer"              
                    return JsonResponse(newserial, safe=False)
            
            else:
                s = {'status': "fail",'reason':"wrong password"} 
                newserial = [] 
                newserial.append(s) 
                return JsonResponse(newserial,safe=False)
    elif garageaccount:
        serializer = garagelogin_serializer(garageaccount,many=True)
        newserial = list(serializer.data)
        for g in garageaccount:
            if bcrypt.checkpw(pw,g.password.encode('utf-8')):
                if serializer.is_valid:
                    newserial[0]['status']="pass"
                    newserial[0]['account type']="garage"             
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
def createGarageAccount(request):
    
    exp = Expert.objects.get(id=request.data.get('expertId'))
    if Garage.objects.all().filter(username=request.data.get('username')):
        newserial = [{'status':"fail",'reason':"account with the username already exists"}]
        return JsonResponse(newserial,safe=False)
    else:
        
        hashed = bcrypt.hashpw(request.data.get('password').encode('utf8'),bcrypt.gensalt())
        account = Garage(expert=exp,name=request.data.get('name'),username=request.data.get('username'),
                        email=request.data.get('email'),phone=request.data.get('phone'),
                        password=hashed.decode('utf8'),address=request.data.get('address'))
        account.save()
        u = User.objects.create_user(username=request.data.get('username'),
                                     password=request.data.get('password'),
                                     is_active=True,is_staff=False)
        
        
        newserial = [{'status':"created"}] 
        return JsonResponse(newserial,safe=False)
    
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def createExpertAccount(request):
    if Expert.objects.all().filter(username=request.data.get('username')):
        newserial = [{'status':"fail",'reason':"account with the username already exists"}]
        return JsonResponse(newserial,safe=False)
    else:
        hashed = bcrypt.hashpw(request.data.get('password').encode('utf8'),bcrypt.gensalt())
        account = Expert(f_name=request.data.get('f_name'),l_name=request.data.get('l_name'),username=request.data.get('username'),
                        p_image=request.data.get('p_image'),email=request.data.get('email'),phone=request.data.get('phone'),
                        password=hashed.decode('utf8'),admin_id=request.data.get('admin_id'))
        account.save()
        u = User.objects.create_user(username=request.data.get('username'),
                                     password=request.data.get('password'),
                                     is_active=True,is_staff=False)
        newserial = [{'status':"created"}] 
        return JsonResponse(newserial,safe=False)
    
    
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def createProposerAccount(request):
    if Proposer.objects.all().filter(username=request.data.get('username')):
        newserial = [{'status':"fail",'reason':"account with the username already exists"}]
        return JsonResponse(newserial,safe=False)
    else:
        hashed = bcrypt.hashpw(request.data.get('password').encode('utf8'),bcrypt.gensalt())
        account = Proposer(f_name=request.data.get('f_name'),l_name=request.data.get('l_name'),
                        username=request.data.get('username'),p_image=request.data.get('p_image'),
                        password=hashed.decode('utf8'))
        account.save()
        u = User.objects.create_user(username=request.data.get('username'),
                                     password=request.data.get('password'),
                                     is_active=True,is_staff=False)
        res_address = ResidentialAddress(account.id,subcity=request.data.get('res_subcity'),
                                            woreda='res_woreda', kebele='res_kebele', house_no='res_house_no',
                                            p_o_box='res_p_o_box', phone='res_phone', email='res_email')
        bus_address = BusinessAddress(account.id,subcity=request.data.get('bus_subcity'),
                                            woreda='bus_woreda', kebele='bus_kebele', house_no='bus_house_no',
                                            p_o_box='bus_p_o_box', phone='bus_phone', email='bus_email',
                                            fax='bus_fax')
        res_address.save()
        bus_address.save()
        newserial = [{'status':"created"}] 
        return JsonResponse(newserial,safe=False)