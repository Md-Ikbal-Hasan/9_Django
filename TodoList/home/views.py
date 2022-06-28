from django.http.response import HttpResponse
from django.shortcuts import render , HttpResponse
from home.models import Contact, Task

# Create your views here.
def home(request):
     context = {'success': False , 'name':'Iqbal'}
     if request.method=="POST":

         title = request.POST['title']
         desc = request.POST['desc']
         print(title,desc)
         ins = Task(taskTitle=title , taskDesc = desc)
         ins.save()
         context = {'success': True }

     return render(request,'index.html', context)

def tasks(request):
    allTasks = Task.objects.all()
    context = {'tasks': allTasks}
   
    return render(request,'tasks.html',context)


def delete_task(request,id):
    pass


def update_task(request,id):
    if request.method=='POST':
        pass
    
        


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