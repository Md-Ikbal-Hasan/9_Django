from xml.dom import ValidationErr
from django import forms
class StudentRegistration(forms.Form):
    name = forms.CharField(label='Your Name' , required=False ,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control some-css'}))
    conf_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control some-css'}))
    roll = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    dept_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'CSE Fundamental'}))

    # custom validation.......
    def clean(self):
        cleaned_data = super().clean()
        valpassword = self.cleaned_data['password']
        valconf_password = self.cleaned_data['conf_password']
        if valpassword != valconf_password:
            raise forms.ValidationError('password and confirm password does not match')

        valname = self.cleaned_data['name']
        if len(valname) <4:
            raise forms.ValidationError('Name is very short')

    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) <4:
    #         raise forms.ValidationError('Name is too short')
        
  
  
  
  
  
    # widgets = {

    #     'name' : forms.TextInput(attrs={'class':'form-control'}),
    #     'email' : forms.EmailInput(attrs={'class':'form-control'}),
    #     'roll' : forms.TextInput(attrs={'class':'form-control'}),
    #     'address' : forms.TextInput(attrs={'class':'form-control'}),
           
    #     }
    
