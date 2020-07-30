from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<em>My Second App<em>')

def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request, 'appTwo/help.html', context=helpdict)
