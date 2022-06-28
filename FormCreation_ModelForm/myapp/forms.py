from django import forms
from .models import User
from django.core import validators

class StudentRegistration(forms.ModelForm):
    name = forms.CharField(max_length=50,required=False , widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['name','password','email']

        labels = {
            'name' :"Enter Your Name",
            'email' : "Enter Your Email",
            'password' : 'Enter Your Password'
        }

        
        # help_text = {
        #     'name' : 'Enter Full Name'
        # }
        

        error_messages = {
            'name' : {'required' : 'name likhe beda'}
        }

        widgets = {
            
            'password' : forms.PasswordInput(attrs= {'class' :'form-control' }),
            'email' : forms.EmailInput(attrs = {'class':'form-control' , 'placeholder' : 'Example : ikbal@gmail.com'}),
        }