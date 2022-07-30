from django import forms
class regi(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    first_name=forms.CharField()