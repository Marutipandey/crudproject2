from django.shortcuts import render

# Create your views here.
def show(request,my_id): 
    print(my_id)  
    return render(request,'enroll/regi.html')