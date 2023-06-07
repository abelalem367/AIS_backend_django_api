from django.urls import path
from . import views
urlpatterns = [
    path('addnewtraffic', views.addNewTraffic),
    path('registeraccident', views.registerAccident)
]
