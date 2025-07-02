from django.contrib import admin
from django.urls import path
from ajaxcrud.views import *

urlpatterns = [
    path('', home, name='home'),
    path('addstu', addstu, name='addstu'),
    path('fetchStudents', fetchStudents, name='fetchStudents')
]