from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome():
    return HttpResponse('<h1>Jay shree Ram ❤️❤️</h1>')
 