from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django import forms
from .models import Student
# Create your views here.

class StudentCreateView(CreateView):
    model = Student
    fields = ['name','email','password']
    # success_url = '/thanks/'

    def get_form(self):
        form  = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Name'})
        form.fields['email'].widget = forms.EmailInput({'class':'form-control'})
        form.fields['password'].widget = forms.PasswordInput({'class':'form-control'})
        return form




class ThanksTemplateView(TemplateView):
    template_name = 'school/thanks.html'



class StudentDetailView(DetailView):
    template_name = 'school/detail.html'
    model = Student