from django.contrib import admin
from myapp.models import *

# Register your models here.

class StudentDisplay(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'age')
    search_fields = ('name', 'email')

admin.site.register(student, StudentDisplay)