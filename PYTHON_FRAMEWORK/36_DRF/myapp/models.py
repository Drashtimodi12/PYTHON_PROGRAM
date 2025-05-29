from django.db import models

# Create your models here.

class stu(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    age = models.IntegerField()
