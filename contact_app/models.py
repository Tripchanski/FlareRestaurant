from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=40)
    post = models.CharField(max_length=25)
    phone_number = models.IntegerField()
    image = models.ImageField(upload_to='images/%Y')