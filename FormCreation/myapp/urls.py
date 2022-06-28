from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
   path('', views.index, name='index'),
   path('login', views.login, name='login')
]