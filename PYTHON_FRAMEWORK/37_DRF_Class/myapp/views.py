from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from myapp.models import *
from myapp.serializer import *

# Create your views here.

class ProductAPI(APIView):
    def get(self, request):
    #     return Response({"message": "GET API called"})
        try:
            allproduct = Product.objects.all()
            ser = ProductSerializer(allproduct, many=True)
            return Response({"data": ser.data})
        except Exception as e:
            return Response({"error": e, "message": "Something went wrong"})

    def post(self, request):
    #     return Response({"message": "POST API called"}) 
        try:
            ser = ProductSerializer(data=request.data)
            if not ser.is_valid():
                return Response({"errors":ser.errors, "message":"Something went wrong"})
            else:
                ser.save()
                return Response({"Inserted data":ser.data})
        except Exception as e:
            return Response({"error": e, "message": "Something went wrong"})

    def put(self, request):
    #     return Response({"message": "UPDATE API called"}) 
        try:
            product = Product.objects.get(pk=request.data.get("id"))
            if not product:
                return Response({"message": "Product not found"})
            else:
                ser = ProductSerializer(product, request.data, partial=True)
                if not ser.is_valid():
                    return Response({"errors":ser.errors, "message":"Something went wrong"})
                else:
                    ser.save()
                    return Response({"Updated data":ser.data})
        except Exception as e:
            return Response({"error": e, "message": "Something went wrong"})
    
    def delete(self, request):
    #     return Response({"message": "DELETE API called"})
        try:
            product = Product.objects.get(pk=request.data.get("id"))
            if not product:
                return Response({"message": "Product not found"})
            else:
                product.delete()
                return Response({"message": "Product deleted successfully"})
        except Exception as e:
            return Response({"error": e, "message": "Something went wrong"})




class ElectricProductAPI(APIView):
    def get(self, request):
        try:
            allelectric = Electric.objects.all()
            ser = ElectricSerializer(allelectric, many = True)
            return Response({"data": ser.data})
        except Exception as e:
            return Response({"error": str(e), "message": "Something went wrong"})
        
    def post(self, request):
        try:
            ser = ElectricSerializer(data=request.data)
            if not ser.is_valid():
                return Response({"errors": ser.errors, "message": "Something went wrong"})
            else:
                ser.save()
                return Response({"Inserted data": ser.data})
        except Exception as e:
            return Response({"error": str(e), "message": "Something went wrong"})
        
    def put(self, request):
        try:
            electric = Electric.objects.get(pk=request.data.get('id'))
            if not electric:
                return Response({"message": "Electric Product not found"})
            else:
                ser = ElectricSerializer(electric, request.data, partial=True)
                if not ser.is_valid():
                    return Response({"errors": ser.errors, "message": "Something went wrong"})
                else:
                    ser.save()
                    return Response({"Updated data": ser.data})
        except Exception as e:
            return Response({"error": str(e), "message": "Something went wrong"})
        
    def delete(self, request):
        try:
            electric = Electric.objects.get(pk=request.data.get('id'))
            if not electric:
                return Response({"message": "Electric Product not found"})
            else:
                electric.delete()
                return Response({"message": "Electric Product deleted successfully"})
        except Exception as e:
            return Response({"error": str(e), "message": "Something went wrong"})