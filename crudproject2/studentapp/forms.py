from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from studentapp import models

class SignUpForm(UserCreationForm):
    class Meta:
        
        #password1  =forms.TextInput(widget=forms.TextInput(attrs={'class' : 'form-control' , 'type':'password'}))
        model = User
        fields = ['username' , 'first_name','last_name','email','password1','password2']

        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'password1' : forms.PasswordInput(attrs={'class':'form-control','type':'password'}), # this field is  from UserCreationForm
           
            #'password1' : forms.TextInput(attrs={'class':'form-control','type':'password'}),

            'password2' : forms.PasswordInput(attrs={'class':'form-control'}),  # from UserCreationForm 
            
        }


class AddStudentForm(forms.ModelForm):
    class Meta:
        model = models.StudentDetails
        fields = "__all__" 
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'phone' : forms.TextInput(attrs={'class':'form-control'}),
            'address' : forms.TextInput(attrs={'class':'form-control'}),
            'class_name' : forms.NumberInput(attrs={'class':'form-control'}), 
            'result' : forms.NumberInput(attrs={'class':'form-control'}),  
              
        }

class UserInfoUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            
        }


