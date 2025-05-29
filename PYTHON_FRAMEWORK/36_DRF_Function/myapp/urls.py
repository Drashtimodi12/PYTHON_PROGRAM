from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    # path('', index, name='index'),
    # path('add', add, name='add'),
    # path('update', update, name='update'),
    # path('delete', delete, name='delete'),

    path('getstudents', index, name='index'),
    path('addstudent', add, name='add'),
    path('updatestudent/<int:id>', update, name='update'),
    path('deletestudent/<int:id>', delete, name='delete'),

    path('viewemployees', indexemployee, name='indexemployee'),
    path('addemployee', addemployee, name='addemployee'),
    path('updateemployee/<int:id>', updateemployee, name='updateemployee'),
    path('deleteemployee/<int:id>', deleteemployee, name='deleteemployee'),
]
