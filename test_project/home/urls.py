from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.add_show,  name="addandshow"),
    path('delete_data/<int:id>/', views.delete_data , name="delete_data"),
    path('update_data/<int:id>',views.update_data, name='update_data'),
]