from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Tenant(models.Model):
    tenant = models.ForeignKey(User,on_delete=models.CASCADE)
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    phone = models.BigIntegerField()

    def __str__(self) -> str:
        return str(self.fname)
    

class Agent(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    phone = models.BigIntegerField()

    def __str__(self) -> str:
        return str(self.fname)
    
class Properties(models.Model):
    TYPE = (
        (1,'Apartment'),
        (2,'Hostel'),
        (3,'Shared Apartment'),
        (5,'Offices'),
        (6,'Mixed Apartment with Offices'),
    )
    AVAILABILITY = (
        (1,'Available'),
        (2,'Booked'),
        (3,'Taken'),
    )
    owner = models.ForeignKey(Agent,on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    location = models.CharField(max_length=25)
    description = models.TextField(max_length=200)
    type = models.IntegerField(choices=TYPE,default=6)
    bedrooms = models.IntegerField()
    size = models.BigIntegerField()
    bathrooms = models.CharField(max_length=25)
    amenities = models.CharField(max_length=25)
    price = models.FloatField()
    availability = models.IntegerField(choices=AVAILABILITY,default=1)
    images = models.ImageField()

    def __str__(self) -> str:
        return str(self.owner)+ '-' + str(self.name)
    
    

