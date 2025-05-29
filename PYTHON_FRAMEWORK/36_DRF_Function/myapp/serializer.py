from rest_framework import serializers
from myapp.models import *

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'
        # fields = ["id","name"]
        # exclude = ["name"]

class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = '__all__'
        # fields = ["id","name"]
        # exclude = ["name"]