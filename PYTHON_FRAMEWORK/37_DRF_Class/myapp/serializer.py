from rest_framework import serializers
from myapp.models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ElectricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Electric
        fields = '__all__'