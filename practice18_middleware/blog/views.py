from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    print("This is home view")
    return HttpResponse("<h1> Hello this is home view </h1>  ")