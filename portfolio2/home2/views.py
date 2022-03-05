from django.http.response import HttpResponse
from django.shortcuts import render
from home2.models import Contact

def home(request):
    #return HttpResponse("This is my home page of new portfolio")
    return render(request,'home.html')

def about(request):
    #return HttpResponse("This is my about page")
    return render(request, 'about.html')

def projects(request):
    #return HttpResponse("This is my projects page")
    return render(request, 'projects.html')

def contact(request):
    if request.method=="POST":

        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        #print(name,email,phone,desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        print("the data has been written to the db")

    #return HttpResponse("This is my contact page")
    return render(request, 'contact.html')
