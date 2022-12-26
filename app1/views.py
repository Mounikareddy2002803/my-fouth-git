from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first(request):
    return HttpResponse('<h3>first view in app1</h3>')
def third(request):
    return HttpResponse('<h3> third view in app1</h3>')