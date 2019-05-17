from django.db import models
from django.db.models.signals import post_save

class Product(models.Model):
    title = models.CharField(max_length= 80)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    avalaiability = models.BooleanField()

class SuperProduct(models.Model):
    title = models.CharField(max_length= 80)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    avalaiability = models.BooleanField()
    website = models.URLField(default="")

