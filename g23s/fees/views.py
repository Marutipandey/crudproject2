from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def feesdj(request):
    return HttpResponse("fees dj  hiiiiiii")

def feespy(request):
    return HttpResponse("fees py  hiiiiiii")