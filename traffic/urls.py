from django.urls import path
from . import views
urlpatterns = [
    path('addnewtraffic', views.addNewTraffic),
    path('registeraccident', views.registerAccident),
    path('gettraffic', views.getTraffics),
    path('changepassword',views.changePassword),
    path('addAdmin',views.addAdmin),
    path('login',views.Login),
    path('sendemail',views.sendEmail)
]
