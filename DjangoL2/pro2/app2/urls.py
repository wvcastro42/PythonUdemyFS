from django.urls import path
from pro2 import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.users, name='users'),
]
