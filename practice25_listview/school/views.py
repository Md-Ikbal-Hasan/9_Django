from urllib import request
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Student
# Create your views here.
class StudentListView(ListView):
    model = Student
    #ordering = ['roll'] # roll onujai order kore database theke dekhabe
    template_name = 'school/student.html'
    context_object_name = 'students'

    def get_queryset(self):
        return Student.objects.filter(roll = '104')

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['freshers'] = Student.objects.all().order_by('name')
        return context

    def get_template_names(self):
        if self.request.COOKIES['user'] == 'ikbal':
            template_name = 'school/ikbal.html'
        else:
            template_name =  self.template_name
        return [template_name]
