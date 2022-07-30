from email.message import Message
from fileinput import FileInput
from django import forms
class regi(forms.Form):
    name=forms.CharField(label='Your Name',help_text="30 ch ho sak hai",widget=forms.PasswordInput())
    photo=forms.CharField(widget=forms.FileInput())
    Message=forms.CharField(widget=forms.Textarea())
    CssUseKeLiye=forms.CharField(widget=forms.Textarea(attrs={'class':'somecss1'}))
    
    