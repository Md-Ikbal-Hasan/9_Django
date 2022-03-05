from django.shortcuts import render, HttpResponse
from blog.models import Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'index.html')   


def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs' : blogs}
    return render(request, 'bloghome.html', context) 


def blogpost(request , slug  ):
    blog = Blog.objects.filter(slug = slug).first
    context = {'blog' : blog}

    return render(request, 'blogpost.html' , context)


def search(request):
    return render(request, 'search.html')


def contact(request):
    return render(request, 'contact.html')

def registration(request):
    form = UserCreationForm
    if request.method=='POST':
        regForm  =UserCreationForm(request.POST)
        if regForm.is_valid():
            regForm.save()
            messages.success(request,'User has been registered')

    return render(request, 'registration.html' , {'form': form})


def login(request):
    return render(request, 'login.html')


