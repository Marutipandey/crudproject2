from django.shortcuts import render
from .forms import student
# Create your views here.
def showformdata(request):
    fm=student(auto_id=True,label_suffix="-",initial={'name':"sonam"})
    return render(request,'enroll/userregistration.html',{'form':fm})