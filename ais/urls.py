from django.urls import path
from . import views
urlpatterns = [
    
    path('login',views.Login),
    path('createvehicleinsurance',views.createVehicleInsurance),
    path('creategarageaccount',views.createGarageAccount),
    path('createexpertaccount',views.createExpertAccount),
    path('createproposeraccount',views.createProposerAccount),
    path('addAdmin',views.addAdmin),
    path('sendemail',views.sendEmail),
    path('getvehicles',views.getVehicles),
    path('getproposers',views.getproposers),
    path('getgarages',views.getgarages),
    path('getexperts',views.getexperts),
    path('getclaims',views.getclaims),
    path('changepassword',views.changePassword),
    path('getcontracts',views.getcontracts),
    path('addvehiclecontract',views.addVehicleContract),
    path('getclaimsbot',views.getclaimsbot),
    path('addclaim',views.addClaim),
    path('updateaccount',views.updateaccount),
    path('createbid',views.createbid),
    path('creategaragebid',views.creategaragebid),
    path('getbid',views.getbid),
    path('getgaragebid',views.getgaragebid),
    path('getproposeremail',views.getproposeremail),
    path('approvecontract',views.approvecontract),
    path('addhealthcontract',views.addhealthcontract),
    path('addhospital',views.addhospital)
]
