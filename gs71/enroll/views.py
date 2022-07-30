from django.shortcuts import render
from .forms import Studentregistration
from django.contrib import messages 

# Create your views here.
def regi(request):
    if request.method=='POST':
      fm=Studentregistration(request.POST)
      if fm.is_valid():
        fm.save()
        messages.add_message(request,messages.SUCCESS,'Your Account has been created !!!')
        messages.info(request,'Now you can login !!!')
    else:
        fm=Studentregistration()
    return render(request,'enroll/userregistration.html',{'form':fm})
    