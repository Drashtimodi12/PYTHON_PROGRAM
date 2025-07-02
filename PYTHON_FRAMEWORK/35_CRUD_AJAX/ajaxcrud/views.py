from django.shortcuts import render
from django.http import HttpResponse
from ajaxcrud.models import *
from django.http import JsonResponse

# Create your views here.

def home(request):
    return render(request, 'home.html') 


def addstu(request):
    if request.method == 'POST':
        data = request.POST
        # print(data)
        name = data.get('name')
        email = data.get('email')
        age = data.get('age')

        Student.objects.create(name=name, email=email, age=age)
        return HttpResponse("Student added successfully!")

def fetchStudents(request):
    alldata = Student.objects.all()
    return JsonResponse({"data": list(alldata.values())})
