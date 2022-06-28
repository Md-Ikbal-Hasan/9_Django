from urllib import request
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Student
# Create your views here.

class StudentList(ListView):
    model = Student
    template_name = 'school/studentlist.html'
    # all_std = Student.objects.all()
   

   
class StudentDetailView(DetailView):
    model = Student
    template_name = 'school/studentdetail.html'
    # context_object_name = 'stu'
    pk_url_kwarg = 'id'
    print(model)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_student'] = Student.objects.all()
        return context