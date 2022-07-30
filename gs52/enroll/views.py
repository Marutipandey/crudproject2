from django.shortcuts import render
from .forms import regi
# Create your views here.
def show(request):
    fm=regi()
    return render(request,'enroll/regi.html',{'form':fm})