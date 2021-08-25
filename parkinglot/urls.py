from django.urls import path

from parkinglot.views import Parkinglot_car,Parkinglot_truck,Parkinglot_main

app_name = "parkinglot"

urlpatterns = [
    path('car/', Parkinglot_car.as_view(), name="car"),
    path('truck/', Parkinglot_truck.as_view(), name="truck"),
    path('', Parkinglot_main.as_view(), name="main")
]