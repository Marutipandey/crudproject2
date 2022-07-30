from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def learndj(request):
    return HttpResponse("course dj  hiiiiiii")

def learnpy(request):
    return HttpResponse("course py  hiiiiiii")