from django.urls import path
from AppTwo import views

urlpatterns = [
    path('help/', views.help, name='help'),
]
