from email.policy import default
from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['name'] = 'Ikbal'
    #request.session['lname'] = 'Hosen'
    return render(request,'student/setsession.html')



def getsession(request):
    #name = request.session['name'] 
    name = request.session['name']
    #keys = request.session.keys()
    #items = request.session.items()
    #age = request.session.setdefault('age','23')
    return render(request,'student/getsession.html',{'name':name})



def delsession(request):
    #if 'name' in request.session:
        #del request.session['name']
    request.session.flush() # the session will be deleted
    return render(request,'student/delsession.html')


