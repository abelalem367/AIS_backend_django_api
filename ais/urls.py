from django.urls import path
from . import views
urlpatterns = [
    path('viewdata', views.getData),
    path('login',views.Login),
    path('createvehicleinsurance',views.createVehicleInsurance),
    path('creategarageaccount',views.createGarageAccount),
    path('createexpertaccount',views.createExpertAccount),
    path('createproposeraccount',views.createProposerAccount),
]
