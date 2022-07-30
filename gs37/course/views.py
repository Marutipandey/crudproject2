from django.shortcuts import render

# Create your views here.
def courseinfo1(request):
    return render(request,'course/courseinfo.html')