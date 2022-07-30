from django.shortcuts import render
from .forms import student
# Create your views here.
def showformdata(request):
    fm=student()
    return render(request,'enroll/userregistration.html',{'form':fm})