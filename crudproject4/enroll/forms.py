from django import forms
from.models import User
class StudentRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['Enter_Your_question','First_Choice','Second_Choice','Third_Choice','Fourth_Choice','Correct_Choice']
        widgets={
        'Enter_Your_question':forms.TextInput(attrs={'class':'form-control'}),
        'First_Choice':forms.TextInput(attrs={'class':'form-control'}),
        'Second_Choice':forms.TextInput(attrs={'class':'form-control'}),
        'Third_Choice':forms.TextInput(attrs={'class':'form-control'}),
        'Fourth_Choice':forms.TextInput(attrs={'class':'form-control'}),
        'Correct_Choice':forms.TextInput(attrs={'class':'form-control'}),
        }
        