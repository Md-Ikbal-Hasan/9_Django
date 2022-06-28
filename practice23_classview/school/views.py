from django.http import HttpResponse
from django.shortcuts import render

from django.http import HttpResponse
from .forms import ContactForm

from django.views import View


# function based view.........
def myview(request):
    return HttpResponse(' <h1>Function based view  </h1>  ')



# class based view.............
class MyView(View):
    name = 'Shaon'
    def get(self,requet):
        # return HttpResponse(' <h1>Class based view - Get </h1>  ')
        return HttpResponse(self.name)


class MyViewChild(MyView): # inherit MyView Class
    def get(self,request):
        return HttpResponse(self.name)



##################################################



def homefun(request):
    return render(request,'school/home.html')


class HomeClassView(View):
    def get(self,request):
        return render(request,'school/home.html')


class AboutClassView(View):
    def get(self,request):
        context = {'msg' :  'Welcome to Django Backend course'}
        return render(request,'school/about.html',context)

        
class ContactClassView(View):
    def get(self,request):
        form = ContactForm()
        return render(request,'school/contact.html' , {'form' : form})

    def post(self,request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            print(name)
            return HttpResponse(name)


