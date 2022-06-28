from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import * 

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length =70)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length = 70)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name' , instance.name)
        instance.roll = validated_data.get('roll' , instance.roll)
        instance.city = validated_data.get('city' , instance.city)

        instance.save()
        return instance


    # field validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat full !')
        return value


    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')

        if nm.lower() =='ikbal' and ct.lower()!='cumilla':
            raise serializers.ValidationError('City should be Cumilla ')
        return data

        
        

