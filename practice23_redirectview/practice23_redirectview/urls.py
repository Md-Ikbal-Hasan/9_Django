"""practice23_redirectview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.TemplateView.as_view(template_name='school/home.html'), name='blankhome'),

    path('home/',views.RedirectView.as_view(url = '/') , name='home'),

    #path('ikbal/',views.RedirectView.as_view(url = 'https://md-ikbal-hasan.github.io/portfolio/') , name='ikbal'),
    path('ikbal/',views.IkbalRedirectView.as_view() , name='ikbal'),
    path('shaon/',views.ShaonRedirectView.as_view() , name='shaon'),


    path('home/<int:pk>/',views.BijoyRiderectView.as_view() , name='bijoy'),
    path('roll/<int:pk>/',views.TemplateView.as_view(template_name='school/home.html'),name='mindex'),

    # path('home/<slug:post>/',views.BijoyRiderectView.as_view() , name='bijoy'),
    # path('<slug:post>/',views.TemplateView.as_view(template_name='school/home.html'),name='mindex'),


    
    path('index/',views.RedirectView.as_view(pattern_name='home') , name='index'),





]
