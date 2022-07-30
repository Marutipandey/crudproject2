from django.shortcuts import render
from .models import Student
from.forms import StudentRegistration
# Create your views here.
def home(request):
     if request.method=='POST':
         fm=StudentRegistration(request.POST)
         if fm.is_valid():
             nm=fm.cleaned_data['studenttname']
             ne=fm.cleaned_data['studenttemail']
             np=fm.cleaned_data['studenttpassword']
             reg=Student(studenttname=nm,studenttemail=ne,studenttpassword=np)
             reg.save()
             fm=StudentRegistration()
     
     else:
       fm=StudentRegistration()
     stud=Student.objects.all()
     return render(request,'enroll/home.html',{'form':fm,'stu':stud})
    






















            
   