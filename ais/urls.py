from django.urls import path
from . import views
urlpatterns = [
    path('viewdata', views.getData),
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
    path('getcontracts',views.getcontracts)
]
