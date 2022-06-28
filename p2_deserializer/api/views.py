from django.shortcuts import render
from .models import *
import io
from requests import request
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from .serializers import StudentSerializer

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body  
        # print("JSON_Data=>   ",json_data)
        stream = io.BytesIO(json_data)
        # print('stream data=>  ', stream)
        pythondata = JSONParser().parse(stream)
        # print("python data=>  ", pythondata)
        serializer = StudentSerializer(data = pythondata)

        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'student created successfully'}

            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')


        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')


    else:
        stu = Student.objects.all()   
        serializer = StudentSerializer(stu,many = True)
        return JsonResponse(serializer.data, safe=False)
