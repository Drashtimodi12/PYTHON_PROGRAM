from django.shortcuts import render
from myapp.models import *
# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):

    if request.method == 'POST':
        data = request.POST
        # print(data)
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        age = data.get('age')

        st = student.objects.create(name=name, email=email, phone=phone, age=age)
        if(st):
            return render(request, 'index.html', {'message': 'Student registered successfully'})
    
    return render(request, 'index.html')