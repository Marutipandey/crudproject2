from django.shortcuts import render

# Create your views here.
def fees_django(request):
    return render(request,'fees/feesone.html',{'title':'fees django','cname':'django'})

def fees_python(request):
    return render(request,'fees/feestwo.html',{'title':'fees python','cname':'python'})