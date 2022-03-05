from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q

from PracticeApp.models import *

# Create your views here.
def index(request):
    #student_data = Student.objects.all()
    #student_data = Student.objects.filter(department=1)
    #student_data = Student.objects.exclude(department=1)

    #student_data = Student.objects.all().order_by('name') # assending order
    #student_data = Student.objects.all().order_by('-name') #descending order
    #student_data = Student.objects.all().order_by('?')  # randomly sorted
    #student_data = Student.objects.all().order_by('id')
    #student_data = Student.objects.all().order_by('id')[:4] # first 4 object
    #student_data = Student.objects.all().order_by('id').reverse()
    #student_data = Student.objects.all().order_by('id').reverse()[:3] # last 3 object

 
    #student_data = Student.objects.values('name','age') #specific column ,  store only name and age of objects, 
    #student_data = Student.objects.values_list() # it retuen tuple , not dictionary
    #student_data = Student.objects.values_list('id' , 'name', named=True) # return id and name of objects
    
    #student_data = Student.objects.filter(id=6) & Student.objects.filter(age=24)
    #student_data = Student.objects.filter(id=5 , age=23) # and operator like previous one
    #student_data = Student.objects.filter(  Q(id=5) & Q(age=23) ) #same , and operation
    
    #student_data = Student.objects.filter(id=7) | Student.objects.filter(age=24)
    
    
    #student_data = Student.objects.filter(name__contains ='ba')
    #student_data = Student.objects.filter(id__in =[1,2,7,9,10])
    #student_data = Student.objects.filter(age__in =[23]) # whose age are 23 they are stored
    #student_data = Student.objects.filter(age__in = [1,2,7,9,10])
    #student_data = Student.objects.filter(age__gt = 23) # age > 23
    #student_data = Student.objects.filter(age__gt = 23 , age__lt = 30)
    #student_data = Student.objects.filter(age__gt = 23 , age__lt = 30).values('name','age')
    #student_data = Student.objects.filter(age__gt = 23 , age__lt = 30).values('name','age').order_by('name')
    # gte = greater than or equal
    # lt less than
    # lte = less than or equal
    #student_data = Student.objects.filter(name__startstwith ='t') # not work . why?
    #student_data = Student.objects.filter(name__istartstwith ='t') # not work

    #print(student_data)
    student_data = Student.objects.all()

    
    math = Course.objects.get(pk=2) # pk of math course =  2
    math_std = math.students.all() # all student of math course
    print("Math Student => " , math_std)

   
    eng = Course.objects.get(pk=3) # pk of eng course =  3
    eng_std = eng.students.all() # all student of eng course
    for std in eng_std:
        print("English student => " , std.name , std.age, std.department , std.department.department_code)
        # how can I print course name also
        #print("English student => " , std.course_set.name,  std.name , std.age, std.department , std.department.department_code)
       
   
    iqbal = Student.objects.get(pk=2)
    iqbal_courses = iqbal.course_set.all()  # all courses of a specific student (Ikbal)
    #print("iqbal's courses list => " , iqbal_courses)
    for course in iqbal_courses:
        print("iqbal course list => " , course.name , course.students.name)

    """ 
    cse_dept = Department.objects.get(pk=1)
    cse_dept_std = cse_dept.student_set.all()  # cse dept all student
    #print("CSE Department Student => "  ,cse_dept_std)
    for std in cse_dept_std:
        print("CSE Department Student => "  ,std.id , std.name , std.age ,std.department)
    """
    

    
    #print('SQL Query =>  ' , student_data.query)
    diction = {'students' : student_data}
    return render(request ,'PracticeApp/index.html' , context=diction)