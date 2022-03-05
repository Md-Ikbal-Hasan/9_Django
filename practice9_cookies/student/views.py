from django.shortcuts import render

# Create your views here.
def setcookie(request):
    response =  render(request, 'student/setcookie.html')
    response.set_cookie('name','Ikbal')
    return response


def getcookie(request):
    pass
