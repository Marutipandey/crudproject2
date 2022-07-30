from django.shortcuts import render

# Create your views here.
def show(request,my_id): 
    student={'id':my_id}  
    return render(request,'enroll/regi.html',student)