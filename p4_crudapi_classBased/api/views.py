from functools import partial
from django import dispatch
from django.shortcuts import render
from django.http import HttpResponse

import json
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from django.views import View

# Create your views here.


@method_decorator(csrf_exempt, name= 'dispatch')
class StudentApi(View):
    def get(self,request, *args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id' , None) # python_data te id ar modde value thake id te store hobe nahole None store hobe
        
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type= 'application/json')


        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type= 'application/json')

    def post(self,request, *args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythondata)

        if serializer.is_valid():
            serializer.save()
            res = {  'msg' : 'Data inserted successfully' }
            json_data = JSONRenderer().render(res)  # json.dumps(res)  
            return HttpResponse(json_data, content_type= 'application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type= 'application/json')


    def put(self,request, *args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)

        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu , data = pythondata ,partial=True)
        

        if serializer.is_valid():
            serializer.save()
            res = {  'msg' : 'Data Updated successfully' }
            json_data = JSONRenderer().render(res)  # json.dumps(res)  
            return HttpResponse(json_data, content_type= 'application/json')

        json_data = JSONRenderer().render(serializer.error)
        return HttpResponse(json_data, content_type= 'application/json')

     

    def delete(self,request, *args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)

        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = { 'msg' : 'Data Deleted Successfully'}
        json_data = JSONRenderer().render(res)  # json.dumps(res)  
        return HttpResponse(json_data, content_type= 'application/json')


    



        
