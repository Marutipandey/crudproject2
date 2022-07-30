from django.shortcuts import render

# Create your views here.
def about1(request):
    return render(request,'core/about.html')

def base1(request):
    return render(request,'core/base.html')

def home1(request):
    return render(request,'core/home.html')