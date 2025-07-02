from django.db import models

# Create your models here.

class Student(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    age = models.PositiveIntegerField()


class Employees(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
