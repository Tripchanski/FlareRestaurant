from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from menu_app.models import Product



    

class Account(models.Model):
    session_key = models.CharField(max_length=32)
    name = models.CharField(max_length=30)
    phone_number = PhoneNumberField(unique = True, null = False, blank = False)
    country = models.CharField(max_length=30, null = True, blank = True)
    adress = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=35)
    cashback = models.CharField(max_length=50)
    user = models.OneToOneField(User, blank = True, null = True, on_delete=models.CASCADE)
    

class CartItem(models.Model):
    account = models.ForeignKey(Account, blank = True, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, blank = True, on_delete=models.CASCADE, null=True)
    count = models.IntegerField()
