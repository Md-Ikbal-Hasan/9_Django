from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import ApplicantsInfo

# Create your views here.
def home(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        birthday = request.POST['birthday']
        job_position = request.POST['job_position']
        gender = request.POST['gender']
        interest = request.POST['interest']
        cover_letter = request.POST['cover_letter']
        cv = request.POST['cv']
        new_applicant = ApplicantsInfo(name=name , email=email , birthday=birthday,job_position=job_position,gender=gender ,interest=interest,cover_letter=cover_letter,cv=cv)
  
        new_applicant.save()
        return HttpResponseRedirect('/')
  

    applicant_info = ApplicantsInfo.objects.all()
    content = {
        'name' : 'ikbal',
        'email' : 'ikbal@gmail.com',
        'birthday' : '23/9/1999',
        'job_position' : 'wenb developer',
        'gender' : 'Male',
        'interest'  : 'Machine Learning',
        'cover_letter' : 'Bla bla ',
        'cv' : "",

    }
    return render(request,'index.html',{'x':content})


def refferel(request):
    return render(request,'refferel.html',context={})
