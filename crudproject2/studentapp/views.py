from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
#from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from .models import *
# Create your views here.

def home(request):
    dict = {'title':'Home Page'}
    return render(request,'studentapp/home.html' , context=dict)
  
def user_sign_up(request):
    
    if request.method=='POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm = SignUpForm()
            messages.success(request,"Account Created Successfully!!!")
        else:
            messages.error(request,"Your data is not valid. Enter valid data carefully!")

    else:
        fm = SignUpForm()

    dict = {'form':fm , 'title':'Sign Up'}
    return render(request,'studentapp/signup.html' , context=dict)
   
   

def user_login(request):
    if not request.user.is_authenticated:

        if request.method=='POST':
            fm = AuthenticationForm(request=request , data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)

                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/profile/')
            else:
                messages.error(request,"Enter correct username and password!!!")
            
        else:
            fm = AuthenticationForm()
    
        dict = {'form':fm , 'title':'Login'}
  
        return render(request,'studentapp/login.html' , context=dict)
    else:
        return HttpResponseRedirect('/profile/')



def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/login/')
    else:
        return HttpResponseRedirect('/login/')


def user_profile(request):
    if request.user.is_authenticated:
        user = request.user
        dict = {'title':'Profile Page','user':user}
        return render(request,'studentapp/profile.html' , context=dict)
    else:
        return HttpResponseRedirect('/login/')

def user_info_update(request,id):
    if request.user.is_authenticated:

        user_info = User.objects.get(pk=id)
        fm = UserInfoUpdateForm(instance=user_info)

        if request.method=='POST':
            fm = UserInfoUpdateForm(request.POST,instance=user_info)
            if fm.is_valid():
                fm.save(commit=True)
                return HttpResponseRedirect('/profile/')
        
        dict = {'form' :fm}
        return render(request,'studentapp/userprofileupdate.html',context=dict)
    else:
        return HttpResponseRedirect('/login/')



def user_change_pass(request):
    if request.user.is_authenticated:
        #return HttpResponse("correct path man!!!")
        
        if request.method=='POST':

            fm = PasswordChangeForm(user=request.user , data = request.POST)
            if fm.is_valid():
                fm.save()  
                #update_session_auth_hash(request , fm.user)
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user = request.user)
        return render(request,'studentapp/userchangepass.html' , {'form':fm})
        
    else:
        return HttpResponseRedirect('/login/')


   
def student_details(request):
    if request.user.is_authenticated:
        students_info = StudentDetails.objects.all()
        dict = {'title':'student details','students_info':students_info}
        return render(request,'studentapp/studentdetails.html' , context=dict)
    else:
        return HttpResponseRedirect('/login/')


def addstudent(request):
    if request.user.is_superuser:

        if request.method=='POST':
            fm =AddStudentForm(request.POST)
            if fm.is_valid():
                fm.save(commit=True)
                return HttpResponseRedirect('/studentdetails/')
            
        else:
            fm = AddStudentForm()

        dict = {'title':'add student', 'form':fm}
        return render(request,'studentapp/addstudent.html' , context=dict)
    
    else:
        return HttpResponseRedirect('/') # go to home page
        

def update_student(request,id):
    if request.user.is_authenticated:
        std_info = StudentDetails.objects.get(pk=id)
        if request.method=='POST':
            fm = AddStudentForm(request.POST,instance=std_info)
            if fm.is_valid():
                fm.save(commit=True)
                return HttpResponseRedirect('/studentdetails/')
        else:
            fm = AddStudentForm(instance=std_info)
        dict = {'form':fm}
        return render(request,'studentapp/updatestudent.html',context=dict)
    else:
        return HttpResponseRedirect('/login/')

def delete_student(request,id):
    std = StudentDetails.objects.get(pk=id)
    std.delete()
    return HttpResponseRedirect('/studentdetails/')