from django.db import models
from menu_app.models import Product

class ProductInCart(models.Model):
    session_key = models.CharField(max_length=32)
    product = models.ForeignKey(Product, blank=True, on_delete=models.CASCADE, null=True)
    count = models.IntegerField()