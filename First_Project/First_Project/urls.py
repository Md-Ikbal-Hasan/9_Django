from django.contrib import admin
from django.urls import path

#from first_app import views  # import view from the first app...............
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('first_app.urls')),

   

]
