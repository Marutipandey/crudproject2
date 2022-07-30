from django.shortcuts import render

# Cre ate your views here.
def fees_python(request):
    cname='radhika'
    duration='4 month'
    seats=10
    details={'nm':cname,'du':duration,'st':seats}
    return render(request,'fees/feesone.html',context=details)


def fees_django(request):
    return render(request,'fees/feestwo.html')