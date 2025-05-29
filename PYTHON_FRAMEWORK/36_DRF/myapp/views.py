from django.shortcuts import render
from myapp.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.serializer import *

# Create your views here.

@api_view(['GET'])
def index(request):
    # return Response("get api calling")
    allstu = stu.objects.all()
    ser = stuSerializer(allstu, many=True)
    return Response({"stu":ser.data})
    

@api_view(['POST'])
def add(request):
    # print(request.data)
    # return Response("post api calling")
    ser = stuSerializer(data=request.data)
    try:
        if not ser.is_valid():
            return Response({"errors":ser.errors, "message":"something went wrong"})
        else:
            ser.save()
            return Response({"data":ser.data, "message":"data inserted successfully"})
    except Exception as e:
        return Response({"error":e, "message":"something went wrong"})

@api_view(['PUT'])
def update(request,id):
    # return Response("put api calling")
    try:
        Stu = stu.objects.get(pk=id)
        ser = stuSerializer(Stu, request.data, partial=True)
        if not ser.is_valid():
            return Response({"errors":ser.errors, "message":"something went wrong"})
        else:
            ser.save()
            return Response({"data":ser.data, "message":"data updated successfully"})
    except Exception as e:
        return Response({"error":e, "message":"something went wrong"})


@api_view(['DELETE'])
def delete(request,id):
    # return Response("delete api calling")
    try:
        Stu = stu.objects.get(pk=id)
        Stu.delete()
        return Response({"success":True})
    except Exception as e:
        return Response({"error":e, "message":"something went wrong"})