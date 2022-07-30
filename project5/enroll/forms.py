from django import forms
from.models import Student
class StudentRegistration(forms.ModelForm):
    class Meta:
        model=Student
        fields=['Question','Choice1','Choice2','Choice3','Choice4','Right_Choice']
        widgets={
        'Question':forms.TextInput(attrs={'class':'form-control'}),
        'Choice1':forms.TextInput(attrs={'class':'form-control'}),
        'Choice2':forms.TextInput(attrs={'class':'form-control'}),
        'Choice3':forms.TextInput(attrs={'class':'form-control'}),
        'Choice4':forms.TextInput(attrs={'class':'form-control'}),
        'Right_Choice':forms.TextInput(attrs={'class':'form-control'}),
        }
        
