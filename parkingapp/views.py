import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

#@method_decorator(csrf_exempt, name='dispatch')
from parkingapp.models import ParkingState

class ParkingView(View):
    def post(self, request):
        data = json.loads(request.body)
        for i in data:
            if ParkingState.objects.filter(location=i).exists()==False:
                if i<=8:
                    Parking_data=ParkingState.objects.create(
                        location=i,
                        state=str(data[i])
                    )
                    Parking_data.save()
            else:
                Parking_data=ParkingState.objects.get(location=i)
                if Parking_data.state != str(data[i]):
                    Parking_data.state = str(data[i])
                    Parking_data.save()
        Parking_tmp=ParkingState.objects.all()
        for data in Parking_tmp :
            if int(data.location)>8:
                print(data)
                data.delete()
        return HttpResponse(status=200)
    def get(self, request):
        Parking_data=ParkingState.objects.values()
        Parking_list=list(Parking_data)
        print(type(Parking_data[0]["location"]))
        print(type(Parking_data))
        print(Parking_list[0:8])
        return JsonResponse({'parks': list(Parking_data)}, status=200)