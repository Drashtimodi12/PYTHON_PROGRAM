from django.contrib import admin
from myapp.models import *

# Register your models here.

class StudentDetails(admin.ModelAdmin):
    list_display=("name","email","phone","age","image")

admin.site.register(Student, StudentDetails)