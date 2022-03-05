from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib import messages # its messages framework
# Create your views here.

def sign_up(request):
    if request.method=='POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account created Successfully !!!')
            fm.save()
    else:
         fm = SignUpForm()
                
    return render(request, 'enroll/signup.html' , context={'form' :fm})