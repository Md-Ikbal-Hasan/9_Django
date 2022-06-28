"""practice23_classview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from school  import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('func', views.myview, name='func'),
    path('cl/', views.MyView.as_view(name='Engr. Ikbal'), name='cl'), # path of class base view
    path('subcl/', views.MyViewChild.as_view(), name='subcl'),


    path('homefun/', views.homefun, name='homefun'),
    path('homecl/', views.HomeClassView.as_view(), name='homecl'),
    path('aboutcl/', views.AboutClassView.as_view(), name='aboutcl'),
    path('contactcl/', views.ContactClassView.as_view(), name='contactcl'),



 

]
