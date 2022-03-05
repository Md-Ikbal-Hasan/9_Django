from tkinter import Widget
from django.core import validators  # for form validator

from django import forms
from .models import User            # from enroll import models   (this import all model)

class StudentRegistration(forms.ModelForm):
    
    class Meta:
        model = User    # je model theke form banate chai sei model ar name. User model ar akti form create korbo tai model  = User   
        #fields = ['name' , 'email' , 'password']
        fields = ('name' , 'email' , 'password')  # fields = "__all__"  (this is for all fields by default).....
        labels = {'name' : 'Enter Your Name'} # customize label name
        erroe_message = {
            'name' : {'required' :'Enter name must'}
            }
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
            'password' : forms.PasswordInput(render_value=True, attrs={'class' : 'form-control'}),
        }





