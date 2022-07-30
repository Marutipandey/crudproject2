from django.shortcuts import render
from .forms import regi
# Create your views here.
def show(request):
    fm=regi(auto_id=True,label_suffix='-',initial={'name':'sonam'})
    fm.order_fields(field_order=['email','name','first_name'])
    return render(request,'enroll/regi.html',{'form':fm})