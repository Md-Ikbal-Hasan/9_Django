from django.contrib import admin
from django.urls import path
from jobapplication import views

# for media file.....
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('refferel', views.refferel, name='refferel'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)