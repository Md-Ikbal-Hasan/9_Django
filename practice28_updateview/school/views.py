from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django import forms
from .models import Student
# Create your views here.

class StudentCreateView(CreateView):
    model = Student
    fields = ['name','email','password']
    success_url = '/student/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student Registration Form'
        return context

    def get_form(self):
        form  = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Name'})
        form.fields['email'].widget = forms.EmailInput({'class':'form-control'})
        form.fields['password'].widget = forms.PasswordInput({'class':'form-control'})
        return form



class StudentListView(ListView):
    model = Student



class ThanksTemplateView(TemplateView):
    template_name = 'school/thanks.html'







class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name','email','password']
    success_url = '/student/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student Update Form'
        return context


    def get_form(self):
        form  = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Name'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control'})
        form.fields['password'].widget = forms.PasswordInput( render_value=True  , attrs={'class':'form-control'})
        return form




class StudentDeleteView(DeleteView):
    model = Student
    success_url = '/student/'