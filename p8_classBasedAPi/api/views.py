from functools import partial
from django.shortcuts import render

from requests import Response, delete  #pip install requests, befor use requests

from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

"""  
to send api data to frontend install cors = cross origin resource sharing
pip install django-cors-headers


"""

class StudentApi(APIView):
    def get(self,request,pk=None, formate=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        return Response(serializer.data)


    def post(self,request,formate=None):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created!'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def put(self,request,pk=None,formate=None):
        id = pk
        stu = Student.objects.get(pk =id)
        serializer = StudentSerializer(stu , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated!'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk=None,formate=None):
        id = pk
        stu = Student.objects.get(pk =id)
        serializer = StudentSerializer(stu , data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partially Data Updated!'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk=None,formate=None):
        id = pk
        stu = Student.objects.get(pk =id)
        stu.delete()
        return Response({'msg' : 'Data Deleted!'})

    








        

        
