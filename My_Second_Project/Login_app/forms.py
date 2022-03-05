from dataclasses import field
from django import forms
from django.contrib.auth.models import User  # import User model from django authorization(administration) ........
from Login_app.models import UserInfo 

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User  # User holo django admin ar akti model .......
        fields = ('username' , 'password','email')  # ai field gulo User model ar built in field.......
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            
        }
      
class UserInfoForm(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields = ('facebook_id' , 'profile_pic')
        widgets = {
            'facebook_id' : forms.TextInput(attrs={'class':'form-control'}),
            'profile_pic' : forms.FileInput(attrs={'class' : 'form-control'}),
            
        }