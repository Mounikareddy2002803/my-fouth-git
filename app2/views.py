from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def second(request):
    return HttpResponse('<h3>second view in app2</h3>')
def four(request):
    return HttpResponse('<h3> fourth view in app2</h3>')