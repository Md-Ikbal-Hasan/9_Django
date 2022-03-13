from django.shortcuts import render
from .models import *
from django.db.models import Q
# Create your views here.
def home(request):
    #student_data = Student.objects.all()
    #student_data = Student.objects.filter(marks=98)
    #student_data = Student.objects.filter(city='Cumilla')
    #student_data = Student.objects.exclude(marks=98)



    #student_data = Student.objects.all().order_by('name') # assending order
    #student_data = Student.objects.all().order_by('-name') #descending order
    #student_data = Student.objects.all().order_by('?')  # randomly ordered
    #student_data = Student.objects.all().order_by('id')
    #student_data = Student.objects.all().order_by('-marks')
    #student_data = Student.objects.all().order_by('id')[:4] # first 4 object
    #student_data = Student.objects.all().order_by('id').reverse()
    #student_data = Student.objects.all().order_by('id').reverse()[:3] # last 3 object




    #student_data = Student.objects.values('name','roll','marks') #specific column ,  store only name and rool and marks of objects, 
    #student_data = Student.objects.values_list() # it retuen tuple , not dictionary
    #student_data = Student.objects.values_list('id' , 'name','marks', named=True) # return id and name of objects
    


    #student_data = Student.objects.using('default')  # like objects.all()
    #student_data = Student.objects.dates('pass_date','month')

    """  
    qs1  =Student.objects.values_list('id','name',  named=True)
    qs2  =Teacher.objects.values_list('id','name', named=True)
    student_data = qs2.union(qs1)
    """  
    

    """   
    qs1  =Student.objects.values_list('id','name',  named=True)
    qs2  =Teacher.objects.values_list('id','name', named=True)
    student_data = qs2.intersection(qs1)
    """

    """  
    qs1  =Student.objects.values_list('id','name',  named=True)
    qs2  =Teacher.objects.values_list('id','name', named=True)
    student_data = qs1.difference(qs2)
    """





    #student_data = Student.objects.filter(id=6) & Student.objects.filter(marks=98)
    #student_data = Student.objects.filter(id=6 , marks=98) # and operator like previous one
    #student_data = Student.objects.filter(  Q(id=6) & Q(marks=98) ) #same , and operation
    
    student_data = Student.objects.filter(id=7) | Student.objects.filter(marks=98) # or operation



    print("Return : " , student_data)
    print()
    print("SQL Query => " , student_data.query)
    return render( request,'school/home.html', {'students':student_data} )