from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('product', ProductAPI.as_view()),

    path('electronic', ElectricProductAPI.as_view()),
]

