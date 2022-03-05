from ast import Pass
from django.shortcuts import render , HttpResponseRedirect
from .forms import SignUpForm,EditUserProfileForm
from django.contrib import messages # its messages framework

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm ,SetPasswordForm,UserChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash



# Create your views here.
# for create/signup user 
def sign_up(request):
    if request.method=='POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account created Successfully !!!')
            fm.save()
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
                    return HttpResponseRedirect('/profile/')

        else: 
            fm  = AuthenticationForm()
        return render(request, 'enroll/userlogin.html' , context={'form' :fm})
    else:
        return HttpResponseRedirect('/profile/')

        



# Profile
def user_profile(request):
    if request.user.is_authenticated: # means logged in
        if request.method=='POST':
            fm  = EditUserProfileForm(request.POST , instance=request.user)
            if fm.is_valid():
                messages.success(request,"Profile Updated Successfully!!!")
                fm.save()

        else:
            fm = EditUserProfileForm(instance=request.user)

        return render(request,'enroll/profile.html' , {'name' : request.user , 'form':fm})
    else:
        return HttpResponseRedirect('/login/')


    
#log out
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')



#password change with old password.........
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method=='POST':

            fm = PasswordChangeForm(user=request.user , data = request.POST)
            if fm.is_valid():
                fm.save()  
                update_session_auth_hash(request , fm.user)
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user = request.user)
        return render(request,'enroll/changepass.html' , {'form':fm})
    else:
        return HttpResponseRedirect('/login/')




    





