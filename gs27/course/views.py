from django.shortcuts import render

# Cre ate your views here.
def learn_python(request):
    coursename={'cname':'hiiiiiii'}
    return render(request,'course/courseone.html',context=coursename)


def learn_django(request):
    return render(request,'course/coursetwo.html')