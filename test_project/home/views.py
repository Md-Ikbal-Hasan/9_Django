from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from multiprocessing import context
from home import forms
from .models import *

# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = forms.StudentRegistration(request.POST)
        if fm.is_valid:
            fm.save(commit=True)
            return HttpResponseRedirect('/')

    else:
        fm = forms.StudentRegistration()

    stud = User.objects.all()
    diction = {'form':fm  , 'stud' : stud}
    return render(request  ,'addandshow.html' , context=diction)
    

def delete_data(requset,id):
    pi = User.objects.get(pk=id)
    #print(pi)
    pi.delete()
    return HttpResponseRedirect('/')

def update_data(request, id):
    diction = {}
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = forms.StudentRegistration(request.POST , instance=pi)
        if fm.is_valid:
            fm.save(commit=True)
            return HttpResponseRedirect('/')

    else:
        pi = User.objects.get(pk=id)
        fm = forms.StudentRegistration(instance=pi)

       

    diction.update({'id':id , 'form':fm})
    return render(request  ,'addandshow.html', context=diction)



