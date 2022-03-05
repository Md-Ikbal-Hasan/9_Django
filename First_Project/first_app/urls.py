
from django.urls import re_path as url   #from django.conf.urls import url   (this was in django version 3)
from django.urls import path

from first_app import views
app_name = 'first_app'  # for relative url....


urlpatterns = [
    #path('function/', views.index_test , name = 'index_test'), # this is for function view
    path('', views.IndexView.as_view() , name = 'index'), # this is for class view
    
   
    
]
