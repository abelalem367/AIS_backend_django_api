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
def Login(request):
    usr = request.data.get("userName")
    pw = request.data.get("password")
    adminaccount = Admin.objects.all().filter(username=usr)
    expertaccount = Expert.objects.all().filter(username=usr)
    proposeraccount = Proposer.objects.all().filter(username=usr)
    garageaccount = Garage.objects.all().filter(username=usr)
    if adminaccount:
        serializer = adminlogin_serializer(adminaccount,many=True)
        newserial = list(serializer.data)
        for a in adminaccount:
            if a.password==pw:
                if serializer.is_valid:
                    s = {'status': "pass",'account type':"admin"} 
                    newserial.append(s)              
                    return JsonResponse(newserial, safe=False)
            
            else:
                s = {'status': "fail",'reason':"wrong password"} 
                newserial = [] 
                newserial.append(s) 
                return JsonResponse(newserial,safe=False)
    if expertaccount:
        serializer = expertlogin_serializer(expertaccount,many=True)
        newserial = list(serializer.data)
        for e in expertaccount:
            if e.password==pw:
                if serializer.is_valid:
                    s = {'status': "pass",'account type':"expert"} 
                    newserial.append(s)              
                    return JsonResponse(newserial, safe=False)
            
            else:
                s = {'status': "fail",'reason':"wrong password"} 
                newserial = [] 
                newserial.append(s) 
                return JsonResponse(newserial,safe=False)
    if proposeraccount:
        serializer = proposerlogin_serializer(proposeraccount,many=True)
        newserial = list(serializer.data)
        for p in proposeraccount:
            if p.password==pw:
                if serializer.is_valid:
                    s = {'status': "pass",'account type':"proposer"} 
                    newserial.append(s)              
                    return JsonResponse(newserial, safe=False)
            
            else:
                s = {'status': "fail",'reason':"wrong password"} 
                newserial = [] 
                newserial.append(s) 
                return JsonResponse(newserial,safe=False)
    if garageaccount:
        serializer = garagelogin_serializer(garageaccount,many=True)
        newserial = list(serializer.data)
        for g in garageaccount:
            if g.password==pw:
                if serializer.is_valid:
                    s = {'status': "pass",'account type':"garage"} 
                    newserial.append(s)              
                    return JsonResponse(newserial, safe=False)
            
            else:
                s = {'status': "fail",'reason':"wrong password"} 
                newserial = [] 
                newserial.append(s) 
                return JsonResponse(newserial,safe=False)
    
def isthereaccount(request):
    proposeraccount = Proposer.objects.all().filter(username=request.data.get('userName'))
    expertaccount = Expert.objects.all().filter(username=request.data.get('userName'))
    adminaccount = Admin.objects.all().filter(username=request.data.get('userName'))
    garageaccount = Garage.objects.all().filter(username=request.data.get('userName'))
    if proposeraccount or expertaccount or adminaccount or garageaccount:
        return True
@api_view(['POST'])
def createGarageAccount(request):
    if isthereaccount:
        newserial = [{'status':"fail",'reason':"account with the username already exists"}]
        return JsonResponse(newserial,safe=False)
    else:
        account = Garage(name=request.data.get('name'),username=request.data.get('username'),
                        email=request.data.get('email'),phone=request.data.get('phone'),
                        password=request.data.get('password'),address=request.data.get('address'))
        account.save()
        newserial = [{'status':"created"}] 
        return JsonResponse(newserial,safe=False)
    
@api_view(['POST'])
def createExpertAccount(request):
    if isthereaccount:
        newserial = [{'status':"fail",'reason':"account with the username already exists"}]
        return JsonResponse(newserial,safe=False)
    else:
        account = Expert(f_name=request.data.get('f_name'),l_name=request.data.get('l_name'),username=request.data.get('username'),
                        p_image=request.data.get('p_image'),email=request.data.get('email'),phone=request.data.get('phone'),
                        password=request.data.get('password'),admin_id=request.data.get('admin_id'))
        account.save()
        newserial = [{'status':"created"}] 
        return JsonResponse(newserial,safe=False)
    
    
@api_view(['POST'])
def createProposerAccount(request):
    if isthereaccount:
        newserial = [{'status':"fail",'reason':"account with the username already exists"}]
        return JsonResponse(newserial,safe=False)
    else:
        account = Proposer(f_name=request.data.get('f_name'),l_name=request.data.get('l_name'),
                        username=request.data.get('username'),p_image=request.data.get('p_image'),
                        password=request.data.get('password'))
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
        newserial = [{'status':"created"}] 
        return JsonResponse(newserial,safe=False)