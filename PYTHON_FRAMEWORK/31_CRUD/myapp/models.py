from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    image = models.ImageField(upload_to='StuProfile', null=True)

    def __str__(self):
        return self.name
    