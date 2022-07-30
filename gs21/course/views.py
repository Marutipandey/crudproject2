from django.shortcuts import render
from django.http import HttpResponse
# Cre.ate your views here.
def learn_django(request):
    return HttpResponse("HELLO")