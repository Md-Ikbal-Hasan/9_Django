from dataclasses import field
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import * 

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name','roll','city']


        
        



