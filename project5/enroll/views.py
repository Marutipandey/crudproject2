from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import StudentRegistration
from.models import Student
def add_show(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm=StudentRegistration()
    else:
       fm=StudentRegistration()
    stud=Student.objects.all()
    return render(request,'enroll/studentdetails.html',{'form':fm,'stu':stud})

