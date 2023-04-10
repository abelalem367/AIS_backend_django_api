from rest_framework.decorators import api_view
from . serializer import *
from . models import *
from django.http import JsonResponse

@api_view(['GET'])
def getData(request):
    items = Admin.objects.all()
    serializer = ais_serializer(items, many=True)
    return JsonResponse(serializer.data,safe=False)


@api_view(['POST']) 
def adminLogin(request):
    usr = request.data.get("userName")
    pw = request.data.get("password")
    credentials = Admin.objects.all().filter(username=usr)
    serializer = adminlogin_serializer(credentials,many=True)
    newserial = list(serializer.data)
    if not credentials:
        s = {'status': "fail"} 
        newserial = [] 
        newserial.append(s) 
        return JsonResponse(newserial,safe=False)
    
    for credential in credentials:
        if credential.password==pw:
            if serializer.is_valid:
                s = {'status': "pass"} 
                newserial.append(s)              
                return JsonResponse(newserial, safe=False)
            
        else:
            s = {'status': "fail"} 
            newserial = [] 
            newserial.append(s) 
            return JsonResponse(newserial,safe=False)

@api_view(['POST'])
def expertLogin(request):
    usr = request.data.get("userName")
    pw = request.data.get("password")
    credentials = Expert.objects.all().filter(username=usr)
    serializer = expertlogin_serializer(credentials,many=True)
    newserial = list(serializer.data)
    if not credentials:
        s = {'status': "fail"} 
        newserial = [] 
        newserial.append(s) 
        return JsonResponse(newserial,safe=False)
    else:
        for credential in credentials:
            if credential.password==pw:
                if serializer.is_valid:
                    s = {'status': "pass"} 
                    newserial.append(s)              
                    return JsonResponse(newserial, safe=False)
                
            else:
                s = {'status': "fail"} 
                newserial = [] 
                newserial.append(s) 
                return JsonResponse(newserial,safe=False)

@api_view(['POST'])
def garageLogin(request):
    usr = request.data.get("userName")
    pw = request.data.get("password")
    credentials = Garage.objects.all().filter(username=usr)
    serializer = garagelogin_serializer(credentials,many=True)
    newserial = list(serializer.data)
    if not credentials:
        s = {'status': "fail"} 
        newserial = [] 
        newserial.append(s) 
        return JsonResponse(newserial,safe=False)
    else:
        for credential in credentials:
            if credential.password==pw:
                if serializer.is_valid:
                    s = {'status': "pass"} 
                    newserial.append(s)              
                    return JsonResponse(newserial, safe=False)
                
            else:
                s = {'status': "fail"} 
                newserial = [] 
                newserial.append(s) 
                return JsonResponse(newserial,safe=False)
        
@api_view(['POST'])
def proposerLogin(request):
    usr = request.data.get("userName")
    pw = request.data.get("password")
    credentials = Proposer.objects.all().filter(username=usr)
    serializer = proposerlogin_serializer(credentials,many=True)
    newserial = list(serializer.data)
    if not credentials:
        s = {'status': "fail"} 
        newserial = [] 
        newserial.append(s) 
        return JsonResponse(newserial,safe=False)
    else:
        for credential in credentials:
            if credential.password==pw:
                if serializer.is_valid:
                    s = {'status': "pass"} 
                    newserial.append(s)              
                    return JsonResponse(newserial, safe=False)
                
            else:
                s = {'status': "fail"} 
                newserial = [] 
                newserial.append(s) 
                return JsonResponse(newserial,safe=False)
      

@api_view(['POST','GET'])
def createGarageAccount(request):
    if request.method == 'POST':
        account = Garage(name=request.data.get('name'),username=request.data.get('username'),
                        email=request.data.get('email'),phone=request.data.get('phone'),
                        password=request.data.get('password'),address=request.data.get('address'))
        account.save()
        newserial = [{'status':"created"}] 
        return JsonResponse(newserial,safe=False)
    else:
        items = Garage.objects.all()
        serilizer = garagelogin_serializer(items,many=True)
        newserial = list(serilizer.data)
        newserial.append({"status":"fetched"})
        return JsonResponse(newserial,safe=False)
@api_view(['POST','GET'])
def createExpertAccount(request):
    if request.method == 'POST':
        account = Expert(f_name=request.data.get('f_name'),l_name=request.data.get('l_name'),username=request.data.get('username'),
                        p_image=request.data.get('p_image'),email=request.data.get('email'),phone=request.data.get('phone'),
                        password=request.data.get('password'),admin_id=request.data.get('admin_id'))
        account.save()
        newserial = [{'status':"created"}] 
        return JsonResponse(newserial,safe=False)
    else:
        items = Expert.objects.all()
        serilizer = expertlogin_serializer(items,many=True)
        newserial = list(serilizer.data)
        newserial.append({"status":"fetched"})
        return JsonResponse(newserial,safe=False)
    
@api_view(['POST'])
def createProposerAccount(request):
    if request.method == 'POST':
        account = Proposer(f_name=request.data.get('f_name'),l_name=request.data.get('l_name'),username=request.data.get('username'),
                           p_image=request.data.get('p_image'),password=request.data.get('password'))
        account.save()

        res_address = ResidentialAddress(account.id,subcity=request.data.get('res_subcity'),
                                         woreda='res_woreda', kebele='res_kebele', house_no='res_house_no',
                                         p_o_box='res_p_o_box', phone='res_phone', email='res_email')
        bus_address = BusinessAddress(account.id,subcity=request.data.get('bus_subcity'),
                                         woreda='bus_woreda', kebele='bus_kebele', house_no='bus_house_no',
                                         p_o_box='bus_p_o_box', phone='bus_phone', email='bus_email',
                                         fax='bus_fax')
        res_address.save()
        bus_address.save()
        newserial = [{'status':"success"}] 
        return JsonResponse(newserial,safe=False)
    else:
        items = Proposer.objects.all()
        serilizer = proposerlogin_serializer(items,many=True)
        newserial = list(serilizer.data)
        newserial.append({"status":"fetched"})
        return JsonResponse(newserial,safe=False)