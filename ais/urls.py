from django.urls import path
from . import views
urlpatterns = [
    path('api/ais/viewdata', views.getData),
    path('api/ais/adminlogin',views.adminLogin),
    path('api/ais/expertlogin/',views.expertLogin),
    path('api/ais/garagelogin/',views.garageLogin),
    path('api/ais/proposerlogin/',views.proposerLogin),
    path('api/ais/creategarageaccount/',views.createGarageAccount),
    path('api/ais/createexpertaccount/',views.createExpertAccount),
    path('api/ais/createproposeraccount/',views.createProposerAccount),
]
