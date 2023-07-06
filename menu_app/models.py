from django.db import models
# from user_app.models import Account

class Product(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/%Y')

class Comment(models.Model):
    username = models.CharField(max_length=30)
    review = models.TextField()
    rating = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)