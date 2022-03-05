from tkinter import Widget
from urllib import request
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'first_name' , 'last_name' , 'email']
        labels  ={ 'email' :'Enter Email Address' , 'first_name':'Enter First Name'  } # thats how label changed  

        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'password1' : forms.PasswordInput(attrs={'class':'form-control'}), # this field is  from UserCreationForm
            'password2' : forms.PasswordInput(attrs={'class':'form-control'}),  # from UserCreationForm
            
            
        }

class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username' ,'first_name' , 'last_name','email','date_joined','last_login']
        labels = {'email':'Email'}
        




         