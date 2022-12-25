from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1(request):
    return HttpResponse('<h2>this is my app1 </h2>')
