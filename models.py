from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# models.py



class BusRoute(models.Model):
    class Meta:
        app_label = 'busapp1' 
    name = models.CharField(max_length=100)
    # Add other fields like source, destination, etc.

class BusSchedule(models.Model):
    class Meta:
        app_label = 'busapp1' 
    route = models.ForeignKey(BusRoute, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField(default=timezone.now)


    # Add other fields as needed



