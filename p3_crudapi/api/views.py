from functools import partial
from django.shortcuts import render
from django.http import HttpResponse

import json
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_api(request):

    if request.method == 'GET':
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



    
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)

        if serializer.is_valid():
            serializer.save()
            res = {  'msg' : 'Data inserted successfully' }
            json_data = JSONRenderer().render(res)  # json.dumps(res)  
            return HttpResponse(json_data, content_type= 'application/json')

        json_data = JSONRenderer().render(serializer.error)
        return HttpResponse(json_data, content_type= 'application/json')




    if request.method == 'PUT':
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



    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)

        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = { 'msg' : 'Data Deleted Successfully'}
        json_data = JSONRenderer().render(res)  # json.dumps(res)  
        return HttpResponse(json_data, content_type= 'application/json')

       
      




        
