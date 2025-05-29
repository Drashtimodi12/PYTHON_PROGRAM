from rest_framework import serializers
from myapp.models import *

class stuSerializer(serializers.ModelSerializer):
    class Meta:
        model = stu
        fields = '__all__'
        # feilds = ['id','name']
        # exclude = ['name']