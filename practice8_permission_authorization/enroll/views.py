from ast import Pass
from email.headerregistry import Group
from django.shortcuts import render , HttpResponseRedirect
from .forms import *
from django.contrib import messages # its messages framework

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm ,SetPasswordForm,UserChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User,Group



# Create your views here.
# for create/signup user 
def sign_up(request):
    if request.method=='POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account created Successfully !!!')
            user = fm.save()
            group = Group.objects.get(name='Editor')
            user.groups.add(group)
    else:
         fm = SignUpForm()
                
    return render(request, 'enroll/signup.html' , context={'form' :fm})



# for user login if request.user.is_authenticated: means registered
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm = AuthenticationForm(request=request , data = request.POST)
            if fm.is_valid():

                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username = uname , password=upass)

                if user is not None:
                    login(request,user)
                    messages.success(request,"Logged in successfully!!!")
                    return HttpResponseRedirect('/dashboard/')

        else: 
            fm  = AuthenticationForm()
        return render(request, 'enroll/userlogin.html' , context={'form' :fm})
    else:
        return HttpResponseRedirect('/dashboard/')

        



# dashboard
def user_dashboard(request):
    if request.user.is_authenticated:
        return render(request,'enroll/dashboard.html' , {'name':request.user.username }) 
          
    else:
        return HttpResponseRedirect('/login/')


    
#log out
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')







