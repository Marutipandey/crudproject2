from dataclasses import field
from email.message import Message
from django import forms
from .models import user

class regi(forms.ModelForm):
    class Meta:
        model=user
        fields=['name','email','password']
        labels={'name':'Enter Name','password':'Enter Password'}
        widgets={
            'password':forms.PasswordInput
        }


    
    
    