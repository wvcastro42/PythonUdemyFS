from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [
    path('', views.users, name='users'),
]
