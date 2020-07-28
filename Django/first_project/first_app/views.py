from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello World!")

def aew_carai(request):
    return HttpResponse("Deu certo, porra!")
