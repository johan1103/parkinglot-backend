from django.db import models

# Create your models here.

class ParkingState(models.Model):
    location = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    create_date = models.DateTimeField(null=True,auto_now_add=True)
    update_date = models.DateTimeField(null=True,auto_now=True)
    car_detail=models.ForeignKey("ParkingCar",on_delete=models.CASCADE,null=True)
    class Meta:
        db_table='parks'


class ParkingCar(models.Model):
    car_type=models.CharField(null=True,max_length=255)
    company=models.CharField(null=True,max_length=255)
    product_type=models.CharField(null=True,max_length=255)