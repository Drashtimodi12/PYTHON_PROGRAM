from django.shortcuts import render
from app15.models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')