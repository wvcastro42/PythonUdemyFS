from django.shortcuts import render

# Create your views here.
from app2.models import User

def index(request):
    return render(request, 'app2/index.html')

def users(request):

    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request, 'app2/users.html', context=user_dict)
