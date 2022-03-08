from email.policy import default
from django.shortcuts import render,HttpResponse

# Create your views here.
def setsession(request):
    request.session['name'] = 'Ikbal'
    #request.session['lname'] = 'Hosen'
    return render(request,'student/setsession.html')



def getsession(request):
    if 'name' in request.session:
        name = request.session['name']
        return render(request,'student/getsession.html',{'name':name})
    else:
        return HttpResponse("Your session has expired.....")



def delsession(request):
        request.session.flush()
        request.session.clear_expired()
        return render(request,'student/delsession.html')
   


