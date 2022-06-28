from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.

def index(request):
    #fm = StudentRegistration(auto_id='some_%s')  # some can be any name
    #fm = StudentRegistration(auto_id=True) # id of every input field of this form will be attribute name
    #fm = StudentRegistration(auto_id='ikbal') #same as True.  id of every input field of this form will be as attribute name
    #fm = StudentRegistration(auto_id=False) # id of every input field and label tag of this form will be removed
    #fm = StudentRegistration(auto_id=True,label_suffix='-')
    #fm = StudentRegistration(auto_id=True,label_suffix='-', initial={'name':'ikbal' , 'email':'ikbal@gmail.com'}) # initial = set the initial value of attribute

    #fm.order_fields(field_order=['password','email','name'])


    

    if request.method =='POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print("data is valid")
            password = fm.cleaned_data['password']
            conf_password = fm.cleaned_data['conf_password']
            print(password,conf_password)
            return HttpResponseRedirect('login')

    else:
        fm =StudentRegistration()

    dict = {
        'title' : 'Form Creation practice',
        'form' :fm
    }
    return render(request,'index.html',context=dict)


def login(request):
    return render(request,'login.html')