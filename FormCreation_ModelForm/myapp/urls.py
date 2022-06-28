from django.urls import path
from myapp.views import *
from myapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('userregistration',views.userregistration,name='userregistration')
]