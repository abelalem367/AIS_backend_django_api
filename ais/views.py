from rest_framework.decorators import api_view
from . serializer import *
from . models import *
from django.http import JsonResponse
import bcrypt
from django.contrib.auth.models import User
from django.contrib.auth import login
from rest_framework.permissions import AllowAny
from rest_framework.decorators import authentication_classes, permission_classes
from django.core.mail import send_mail
from django.conf import settings

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

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def getData(request):
    items = Admin.objects.all()
    serializer = ais_serializer(items, many=True)
    return JsonResponse(serializer.data,safe=False)
   
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def getVehicles(request):
    items = Vehicle.objects.all()
    serializer = vehicle_serializer(items, many=True)
    return JsonResponse(serializer.data,safe=False)
    
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def getproposers(request):
    items = Proposer.objects.all()
    serializer = proposerlogin_serializer(items, many=True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def getgarages(request):
    items = Garage.objects.all()
    serializer = garagelogin_serializer(items, many=True)
    return JsonResponse(serializer.data,safe=False)
    
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def getexperts(request):
    items = Expert.objects.all()
    serializer = expertlogin_serializer(items, many=True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def getclaims(request):
    items = Claim.objects.all()
    serializer = claim_serializer(items, many=True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def getclaimsbot(request):
    items = Claim.objects.all().filter(proposer_id=request.data.get("proposerID"))
    if items:    
        serializer = claim_serializer(items, many=True)
        return JsonResponse(serializer.data,safe=False)
    else:
        newserial = [{'status':"fail, no claims found using the given proposerID"}] 
        return JsonResponse(newserial,safe=False)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def getcontracts(request):
    items = VehicleContract.objects.all()
    serializer = vehiclecontract_serializer(items, many=True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def addVehicleContract(request):
    veh_id = Vehicle.objects.get(id=request.data.get('vehicle_id'))
    proposer_id = Proposer.objects.get(id = request.data.get('proposer_id'))
    contr_id = VehicleContract.objects.all().filter(vehicle=request.data.get('vehicle_id'))
    if contr_id:
        newserial = [{'status':"fail",'reason':"account with the vehicle id is already registered"}]
        return JsonResponse(newserial,safe=False)
    else:
        v = VehicleContract(vehicle=veh_id,proposer=proposer_id,contract_type=request.data.get('contractType'),
                        contract_price=request.data.get('contractPrice'),contract_date=request.data.get('contractDate'),
                        expire_date= request.data.get('expireDate'),is_approved=request.data.get('isApproved'))
        v.save()
        newserial = [{'status':"created"}] 
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
                                     is_active=True,is_staff=True)
        u.save()
        newserial = [{'status':"created"}] 
        return JsonResponse(newserial,safe=False) 


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def addClaim(request):
    veh = Vehicle.objects.get(id=request.data.get('vehicleId'))
    gar = Garage.objects.get(id=request.data.get('garageId'))
    prop = Proposer.objects.get(id = request.data.get('proposerId'))
    if Claim.objects.all().filter(accident_id=request.data.get('accident_id')):
        newserial = [{'status':"fail",'reason':"claim with the accident id already submitted"}]
        return JsonResponse(newserial,safe=False)
    else:
        claimobject = Claim(date=request.data.get('date'),accident_id = request.data.get('accident_id'),
        total_price=request.data.get('totalPrice'),closed_date=request.data.get('closedDate'),
        progress=request.data.get('progress'),proposer=prop,garage=gar,vehicle=veh)
        claimobject.save()
        newserial = [{'status':"created"}] 
        return JsonResponse(newserial,safe=False) 
    
    
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
                    newserial[0]['accounttype']="proposer"   
                    
                    newserial[0]['proposerID']=p.id           
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
        
        u.save()
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
        u.save()
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
        u.save()
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

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def updateaccount(request):
    usr = request.data.get("username")
    adminaccount = Admin.objects.all().filter(username=usr)
    expertaccount = Expert.objects.all().filter(username=usr)
    proposeraccount = Proposer.objects.all().filter(username=usr)
    garageaccount = Garage.objects.all().filter(username=usr)
    if adminaccount:
        adminaccount = Admin.objects.get(username=usr)
        adminaccount.f_name = request.data.get('f_name')
        adminaccount.l_name = request.data.get('l_name')
        adminaccount.email = request.data.get('email')
        adminaccount.phone = request.data.get('phone')
        adminaccount.save()
    elif garageaccount:
        garageaccount = Garage.objects.get(username=usr)
        garageaccount.name = request.data.get('name')
        garageaccount.address = request.data.get('address')
        garageaccount.email = request.data.get('email')
        garageaccount.phone = request.data.get('phone')
        garageaccount.save()
    elif expertaccount:
        expertaccount = Expert.objects.get(username=usr)
        expertaccount.f_name = request.data.get('f_name')
        expertaccount.l_name = request.data.get('l_name')
        expertaccount.email = request.data.get('email')
        expertaccount.phone = request.data.get('phone')
        expertaccount.save()
    elif proposeraccount:
        proposeraccount = Proposer.objects.get(username=usr)
        proposeraccount.f_name = request.data.get('f_name')
        proposeraccount.l_name = request.data.get('l_name')
        expertaccount.save()
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
    proposeraccount = Proposer.objects.all().filter(username=typeid)
    expertaccount = Expert.objects.all().filter(username=typeid)
    garageaccount = Garage.objects.all().filter(username=typeid)
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
            
        
    elif proposeraccount:
        for t in proposeraccount:
            if bcrypt.checkpw(pw,t.password.encode('utf-8')):
                passwordchecker='password matches'
                hashed = bcrypt.hashpw(newpw,bcrypt.gensalt())
                myproposerobject = Proposer.objects.get(username = typeid)
                u = User.objects.get(username = typeid)
                if u:
                    u.set_password(newpw.decode('utf8'))
                    u.save()
                myproposerobject.password = hashed.decode('utf8')
                myproposerobject.save()
        if passwordchecker=='password does not match':
            passwordchecker = 'wrong old password'

        
    elif expertaccount:
        for c in expertaccount:
            if bcrypt.checkpw(pw,c.password.encode('utf-8')):
                passwordchecker='password matches'
                hashed = bcrypt.hashpw(newpw,bcrypt.gensalt())
                myexpertobject = Expert.objects.get(username = typeid)
                u = User.objects.get(username = typeid)
                if u:
                    u.set_password(newpw.decode('utf8'))
                    u.save()
                myexpertobject.password = hashed.decode('utf8')
                myexpertobject.save()
        if passwordchecker=='password does not match':
            passwordchecker = 'wrong old password'
    elif garageaccount:
        for c in garageaccount:
            if bcrypt.checkpw(pw,c.password.encode('utf-8')):
                passwordchecker='password matches'
                hashed = bcrypt.hashpw(newpw,bcrypt.gensalt())
                mygarageobject = Garage.objects.get(username = typeid)
                u = User.objects.get(username = typeid)
                if u:
                    u.set_password(newpw.decode('utf8'))
                    u.save()
                mygarageobject.password = hashed.decode('utf8')
                mygarageobject.save()
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

