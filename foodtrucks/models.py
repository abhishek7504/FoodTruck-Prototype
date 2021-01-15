from django.db import models

class FoodType(models.Model):
    foodtype = models.CharField(max_length=50)

    def __str__(self):
        return self.foodtype

class FoodTruck(models.Model):
    foodtype = models.ForeignKey(FoodType,on_delete = models.CASCADE,related_name = 'food_truck')
    location = models.CharField(max_length=100,null=True)
    owner_name = models.CharField(max_length=50,null=True)
    truck_image = models.ImageField(null=True)
    opening_time = models.CharField(max_length=50)
    closing_time = models.CharField(max_length=50)

    def __str__(self):
        return self.owner_name
