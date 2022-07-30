from dataclasses import field

from django import forms
from .models import Student

class StudentRegistration(forms.ModelForm):
    class Meta:
        model=Student
        fields=['studenttname','studenttemail','studenttpassword']
        widgets={
        'studenttname':forms.TextInput(attrs={'class':'form-control'}),
        'studenttemail':forms.EmailInput(attrs={'class':'form-control'}),
        'studenttpassword':forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
        }