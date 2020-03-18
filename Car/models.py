from django.db import models

# Create your models here.

class Car(models.Model):
    car_mark = models.CharField(max_length=30)
    car_production_year = models.CharField(max_length=4)
    car_price = models.CharField(max_length=30)
    car_owner_name = models.CharField(max_length=30)
    car_hp = models.CharField(max_length=30)
    car_number_of_doors = models.CharField(max_length=5)