from django.urls import path, re_path as url
from blog import views
app_name = 'blog'
urlpatterns = [

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('addpost/', views.add_post, name='addpost'),
    path('updatepost/<int:id>', views.update_post, name='updatepost'),
    path('deletepost/<int:id>', views.delete_post, name='deletepost'),
    
    
    

]
