from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import StudentRegistration
from.models import User
# Create your views here.

#add new item and show all items
def add_show(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm=StudentRegistration()
    else:
       fm=StudentRegistration()
    stud=User.objects.all()
    return render(request,'enroll/home.html',{'form':fm,'stu':stud})

