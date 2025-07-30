from django.shortcuts import render, redirect
from myapp.models import *
import os
# Create your views here.

def home(request):
    allstudents = student.objects.all()
    return render(request,'home.html', {'students': allstudents})

def register(request):
    
    if request.method == 'POST':
        data = request.POST
        # print(data)
        stid = data.get('id')     # Get ID from form (if present)
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        age = data.get('age')
        image = request.FILES.get['file']  # Get the uploaded file from the form

        if id:  # If stid is provided, it means update
            Student = student.objects.get(pk=id)
            Student.name=name
            Student.email= email
            Student.phone=phone
            Student.age=age    
            os.remove(Student.image.path)  # Remove the old image file
            Student.image=request.FILES.get['file']  # Update the image if a new one is uploaded
            Student.save()
            return redirect("home")
        else:
            st =  student.objects.create(name=name,email=email,phone=phone,age=age,image=image)
            if st:
                #return render(request,'home.html',{"msg":"Registration successful"})
                return redirect("home")

    return render(request,'home.html')


def delete(request):
    id =  request.GET['id']
    Student = student.objects.get(pk=id)
    os.remove(Student.image.path)  # Delete the image file from the filesystem
    Student.delete()
    return redirect("home")

def update(request):
    id =  request.GET['id']
    Student = student.objects.get(pk=id)
    allstudents  = student.objects.all()
    return render(request,"home.html", {"Student": Student, "students": allstudents})