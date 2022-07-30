from django import forms
class regi(forms.Form):
    name=forms.CharField(label='Your Name',initial='radhe',help_text="is field me 30 char ho sakate hai",disabled=True)
    