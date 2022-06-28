
from django.shortcuts import render , HttpResponseRedirect
from multiprocessing import context  # for passing dictionary through context........
from enroll import forms  # it import all forms from forms.py file   =>  another way(from forms. import StudentRegistration) -> import StudentRegistration form )
from .models import *     # import all models


# Create your views here.

#this function add and show student..........
#this function add and show student..........
def add_show(request): 
    if request.method == 'POST':
        fm = forms.StudentRegistration(request.POST)
        if fm.is_valid:
            fm.save(commit=True)
            #nm = fm.cleaned_data['name']
            #em = fm.cleaned_data['email']
            #pw = fm.cleaned_data['password']
            #reg = User(name=nm  ,email =em , password = pw)
            #reg.save()
            fm = forms.StudentRegistration()   # for clean the form
            
    else:
        fm = forms.StudentRegistration()  # fm = StudentRegistration()  (this was in django 3 version)

    stud = User.objects.all()
    diction = {'form':fm  , 'stud' : stud}
    return render(request  ,'enroll/addandshow.html' , context=diction)



def delete_data(requset,id):
   
    pi = User.objects.get(pk=id)
    pi.delete()
    return HttpResponseRedirect('/')
   

def update_data(request, id):
    diction = {}
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = forms.StudentRegistration(request.POST , instance=pi)
        if fm.is_valid:
            fm.save(commit=True)
            diction.update({'success_text':'Successfully Updated.....'})

    else:
        pi = User.objects.get(pk=id)
        fm = forms.StudentRegistration(instance=pi)

       

    diction.update({'id':id , 'form':fm})
    return render(request  ,'enroll/updatestudent.html', context=diction)

     

   
       
        