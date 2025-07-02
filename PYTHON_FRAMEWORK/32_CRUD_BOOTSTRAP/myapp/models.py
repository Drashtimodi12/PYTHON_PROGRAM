from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    age = models.IntegerField()
    image = models.ImageField(upload_to="Profile")