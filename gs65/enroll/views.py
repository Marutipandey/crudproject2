from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import regi
# Create your views here.
def show(request):
    if request.method=='POST':
       fm=regi(request.POST)
       if fm.is_valid():
           nm=fm.cleaned_data['name']
           em=fm.cleaned_data['email']
           pw=fm.cleaned_data['password']
           print(nm)
           print(em)
           print(pw)
    else:
        fm=regi()
    return render(request,'enroll/regi.html',{'form':fm})