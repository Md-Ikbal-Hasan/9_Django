from django.urls import URLPattern, re_path as path
from django.urls import path
from studentapp import views
app_name = 'studentapp'

urlpatterns= [
    path('',views.home, name='home'),
    path('signup/' ,views.user_sign_up, name='signup'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.user_profile, name='profile'),    
    path('logout/', views.user_logout, name='logout'),
    
    path('userupdate/<int:id>', views.user_info_update, name='userupdate'),
    path('userchangepass/', views.user_change_pass, name='userchangepass'),
    path('addstudent/', views.addstudent, name='addstudent'),
    path('studentdetails/', views.student_details, name='studentdetails'), 
    path('updatestudent/<int:id>', views.update_student, name='updatestudent'), 
    path('deletestudent/<int:id>', views.delete_student, name='deletestudent'),  

]