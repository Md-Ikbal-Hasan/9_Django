from xml.dom.minidom import Document
from django.conf import settings
from django.urls import re_path as url   #from django.conf.urls import url   (this was in django version 3)
from django.urls import path
from Login_app import views

from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns


app_name = 'Login_app'

urlpatterns = [
    path('' , views.index , name = 'index'),
    path('register/' , views.register , name = 'register'),
    path('login/' , views.login_page , name = 'login'),
    path('user_login/' , views.user_login , name = 'user_login'),
    path('logout/' , views.user_logout , name = 'logout'),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)