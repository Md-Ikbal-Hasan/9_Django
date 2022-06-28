from unicodedata import name
from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):

    #student_data = Student.objects.get(pk=8)
    #student_data = Student.objects.get(name="Rafi")

    #student_data = Student.objects.first()
    #student_data = Student.objects.last()

    #student_data = Student.objects.latest('pass_date')
    #student_data = Student.objects.earliest('pass_date')

    #student_data = Student.objects.all()
    #print(student_data.exists()) # true or false

    #s = Student(name='Alhaj',roll='110',city='Rajbari',marks=78,pass_date = '2020-5-4')
    #s.save()

    #s = Student.objects.create(name='Aminul',roll='111',city='Tangail',marks=74,pass_date = '2020-5-27')
    #student_data,created = Student.objects.get_or_create(name='Anisa',roll='112',city='Jessore',marks=74,pass_date = '2020-5-27')
    #student_data = Student.objects.filter(id=11).update(marks=93,city='Noakhali')
    student_data = Student.objects.filter(id=11).update(marks=93,city='Noakhali')
    


    """  
    objs = [
        Student(name='Sakil',roll=113,city='Cumilla',marks=67,pass_date='2020-7-23'),
        Student(name='Lakhi',roll=114,city='Dhaka',marks=90,pass_date='2020-3-23'),
        Student(name='Abdullah',roll=115,city='Dhaka',marks=97,pass_date='2021-7-23'),
    ]
    student_data = Student.objects.bulk_create(objs)
    """
    #student_data = Student.objects.get(pk=11).delete()

    #student_data = Student.objects.all()
    #print(student_data.count())


    


    print("Return : " , student_data)
    return render( request,'school/home.html', {'student':student_data} )