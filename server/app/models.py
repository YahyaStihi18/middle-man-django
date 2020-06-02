from django.db import models
from phonenumber_field.modelfields import  PhoneNumberField
import datetime


# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = PhoneNumberField()
    address = models.CharField(max_length=200, null=True,blank=True)
    image = models.ImageField(default='sp.png')

    def __str__(self):
        return self.name

class Product(models.Model):
    supplier = models.ForeignKey(Supplier,on_delete=models.SET_NULL,null=True,blank=True)
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0.00)
    klm = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    date = models.DateField(default= datetime.date.today)
    image = models.ImageField(default='box.jpg')
    image1 = models.ImageField(null=True,blank=True)
    image2 = models.ImageField(null=True,blank=True)
    image3 = models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.name
    

    
