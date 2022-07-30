from django.shortcuts import render

# Cre ate your views here.
def learn_python(request):
    return render(request,'course/courseone.html')


def learn_django(request):
    return render(request,'course/coursetwo.html')