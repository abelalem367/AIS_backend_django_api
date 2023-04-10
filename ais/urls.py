from django.urls import path
from . import views
urlpatterns = [
    path('viewdata', views.getData),
    path('adminlogin',views.adminLogin),
    path('expertlogin/',views.expertLogin),
    path('garagelogin/',views.garageLogin),
    path('proposerlogin/',views.proposerLogin),
    path('creategarageaccount/',views.createGarageAccount),
    path('createexpertaccount/',views.createExpertAccount),
    path('createproposeraccount/',views.createProposerAccount),
]
