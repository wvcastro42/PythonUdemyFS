from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User

def index(request):
    index_dict = {'index_insert':'Index Page'}
    return render(request, 'appTwo/index.html', context=index_dict)

def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request, 'appTwo/help.html', context=helpdict)

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request, 'appTwo/users.html', context=user_dict)
