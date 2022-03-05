from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from blog.forms import * 
from blog.models import *

# Create your views here.

# Home page view .....................................
def home(request):
    posts = Post.objects.all()
    return render(request,'blog/home.html',context={'posts':posts})



# About ...............................................
def about(request):
    return render(request,'blog/about.html',context={})




# Contact ..............................................
def contact(request):
    return render(request,'blog/contact.html',context={})


# Dashboard for admin and user..........................
def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()

        return render(request,'blog/dashboard.html',context={'posts':posts})
    else:
        return HttpResponseRedirect('/login/')



# User Signup ........................................
def user_signup(request):
    if not request.user.is_authenticated:

        if request.method=='POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                messages.success(request,'Congratulations! You have become an author!!!')
                form.save(commit=True)
                form = SignUpForm() # for clear the form after account created successfully.....
        else:
            form = SignUpForm()

        return render(request,'blog/signup.html',context={'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')




# User Login...........................................
def user_login(request):
    if not request.user.is_authenticated:

        if request.method=='POST':
            form = LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname , password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Successfully Logged in!!')
                    return HttpResponseRedirect('/dashboard/')

        else:
            form = LoginForm()

        return render(request,'blog/login.html',context={'form':form})
    
    else:
        return HttpResponseRedirect('/dashboard/')




# User logout ...............................
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')




# Add new post...............................
def add_post(request):
    if request.user.is_authenticated:

        if request.method=='POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                pst = Post(title=title , desc= desc)
                pst.save()
                form = PostForm()
        else:
            form = PostForm()

        return render(request,'blog/addpost.html', {'form':form})
        
    else:
        return HttpResponseRedirect('/login/')




# Update new post...............................
def update_post(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pst = Post.objects.get(pk=id)
            form = PostForm(request.POST , instance = pst)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            pst = Post.objects.get(pk=id)
            form = PostForm(instance=pst)
        return render(request,'blog/updatepost.html',{'form':form})
        
    else:
        return HttpResponseRedirect('/login/')

# Delete post...................................
def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pst = Post.objects.get(pk=id)
            #print(pst.title)
            pst.delete()
            return HttpResponseRedirect('/dashboard/')
         
        
    else:
        return HttpResponseRedirect('/login/')

