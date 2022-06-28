from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.db.models import Avg,Sum,Min,Max,Count


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
    
    #student_data = Student.objects.filter(id=7) | Student.objects.filter(marks=98) # or operation



    ################# QuerySet API Field Lookups in Django    ###########################

    #student_data = Student.objects.filter(name__contains ='ba')
    #student_data = Student.objects.filter(id__in =[1,2,7,9,10])
    #student_data = Student.objects.filter(marks__in =[98,74])
    #student_data = Student.objects.filter(marks__gt = 80) 
    #student_data = Student.objects.filter(marks__lt = 70)
    #student_data = Student.objects.filter(marks__gt = 70 , marks__lt = 80).values('name','roll','marks')
    #student_data = Student.objects.filter(marks__gt = 80 , marks__lt = 100).values('name','roll','marks').order_by('roll')
    # gte = greater than or equal
    # lt less than
    # lte = less than or equal

    #student_data = Student.objects.filter(name__startstwith ='P') # not work . why?
    #student_data = Student.objects.filter(name__istartstwith ='t') # not work

    #student_data = Student.objects.filter(pass_date__range=('2022-03-03', '2022-03-17'))

    
    ##############   QuerySet API Aggregation in Django  ##########################
    student_data = Student.objects.all()
    
    average = student_data.aggregate(Avg('marks'))
    total = student_data.aggregate(Sum('marks'))
    minimum = student_data.aggregate(Min('marks'))
    maximum = student_data.aggregate(Max('marks'))
    totalcount = student_data.aggregate(Count('marks'))


    print('Average marks : ' , average)
    print('Total marks : ' , total)
    print('minimum marks : ' , minimum)
    print('maximum marks : ' , maximum)
    print('Total Count : ' , totalcount)




    print("Return : " , student_data)
    print()
    print("SQL Query => " , student_data.query)
    return render( request,'school/home.html', {'students':student_data} )