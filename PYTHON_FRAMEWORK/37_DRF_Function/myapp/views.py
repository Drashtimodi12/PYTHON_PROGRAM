from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.models import *
from myapp.serializer import *

# Create your views here.

@api_view(['GET'])
def index(request):
    # return Response({"message": "GET API is working fine!"})
    allstudents = student.objects.all()
    ser = studentSerializer(allstudents, many=True)
    return Response({"students":ser.data})

@api_view(['POST'])
def add(request):
    # return Response({"message": "POST API is working fine!"})
    try:
        ser = studentSerializer(data=request.data)
        if not ser.is_valid():
            return Response({"errors": ser.errors, "message": "Invalid data"})
        else:
            ser.save()
            return Response({"data": ser.data, "message": "Student added successfully!"})
    except Exception as e:
        print(e)
        return Response({"error": e, "message": "An error occurred"})

@api_view(['PUT'])
def update(request,id):
    # return Response({"message": "PUT API is working fine!"})
    try:
        Student = student.objects.get(pk=id)
        ser = studentSerializer(Student, request.data, partial=True)
        if not ser.is_valid():
            return Response({"errors": ser.errors, "message": "Invalid data"})
        else:
            ser.save()
            return Response({"data": ser.data, "message": "Student updated successfully!"})
    except Exception as e:
        return Response({"error": e, "message": "An error occurred"})


@api_view(['DELETE'])
def delete(request,id):
    # return Response({"message": "DELETE API is working fine!"})
    try:
        Student = student.objects.get(pk=id)
        Student.delete()
        return Response({"success": True})
    except student.DoesNotExist:
        return Response({"message": "Student not found"})
    except Exception as e:
        return Response({"error": e, "message": "An error occurred"})
    









@api_view(['GET'])
def indexemployee(request):
    # return Response({"message": "GET API for employees is working fine!"})
    try: 
        allemployees = employee.objects.all()
        ser = employeeSerializer(allemployees, many=True)
        return Response({"employees": ser.data})
    except Exception as e:
        return Response({"error": e, "message": "An error occurred while fetching employees"})

@api_view(['POST'])
def addemployee(request):
    try:
        ser = employeeSerializer(data=request.data)
        if not ser.is_valid():
            return Response({"errors": ser.errors, "message": "Invalid data"})
        else:
            ser.save()
            return Response({"data": ser.data, "message": "Employee added successfully!"})
    except Exception as e:
        return Response({"error": str(e), "message": "An error occurred while adding employee"})
    
@api_view(['PUT'])
def updateemployee(request,id):
    try:
        Employee = employee.objects.get(pk=id)
        ser = employeeSerializer(Employee, request.data, partial=True)
        if not ser.is_valid():
            return Response({"errors": ser.errors, "message": "Invalid data"})
        else:
            ser.save()
            return Response({"data": ser.data, "message": "Employee updated successfully!"})
    except Exception as e:
        return Response({"error": str(e), "message": "An error occurred while updating employee"})
    
@api_view(['DELETE'])
def deleteemployee(request,id):
    try:
        Employee = employee.objects.get(pk=id)
        Employee.delete()
        return Response({"success": True, "message": "Employee deleted successfully!"})
    except Exception as e:
        return Response({"error": e, "message": "An error occurred while deleting employee"})  