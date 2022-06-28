from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import StudentRegistration
from .models import *
# Create your views here.
def index(request):
    return render(request,'index.html',context={})


def userregistration(request):
    if request.method=='POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            #print(name,email,password)
            obj = User(name=name, email= email , password = password)
            obj.save()
            return HttpResponseRedirect('userregistration')
    else:
        fm = StudentRegistration()

    dict = {
        'title' : 'FormCreation using ModelForm',
        'form'  :fm
    }

    return render(request, 'userregistration.html',context=dict)