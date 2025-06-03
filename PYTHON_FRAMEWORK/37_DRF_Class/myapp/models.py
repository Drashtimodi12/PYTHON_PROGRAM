from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()   
    stock = models.IntegerField()

class Electric(models.Model):
    company = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()