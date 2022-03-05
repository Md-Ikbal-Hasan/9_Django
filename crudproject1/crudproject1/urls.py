"""crudproject1 URL Configuration

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


from unicodedata import name
from django.contrib import admin
from django.urls import path
from enroll import views

from django.conf.urls import include

#app_name = 'enroll'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.add_show , name="addandshow"),
    path('delete_data/<int:id>/', views.delete_data , name="delete_data"),
    path('<int:id>', views.update_data , name="update_data"),
]
