from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Vendor(models.Model):
    profile= models.ImageField(upload_to='images/',null=True, blank=True)
    address=models.TextField(max_length=300,blank=False)
    phone_no=models.IntegerField()


class Customer(models.Model):
    profile= models.ImageField(upload_to='images/',null=True, blank=True)
    address=models.TextField(max_length=300,blank=False)
    phone_no=models.IntegerField()

