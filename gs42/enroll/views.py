from django.shortcuts import render
from enroll.models import Student
# Create your views here.
def studentinfo(request):
    stud=Student.objects.all()
    # only one row ki value show karane ke liye stud=Student.objects.get(pk=2)
    return render(request,'enroll/studentdetails.html',{'stu':stud})
    