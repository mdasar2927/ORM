from django.db import models
from django.contrib import admin

class Car(models.Model):
    car_brand = models.CharField()
    car_model = models.CharField()
    year = models.DateField()
    color = models.CharField()
    engine_type = models.CharField()
    fuel_type = models.CharField()
    transmission = models.CharField()
    seating_capacity = models.IntegerField()
    price = models.CharField()
    description = models.TextField()

class CarAdmin(admin.ModelAdmin):
    list_display = ('car_brand', 'car_model', 'year', 'color', 'engine_type', 'fuel_type', 'transmission', 'seating_capacity', 'price', 'description')