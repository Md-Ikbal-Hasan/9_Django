from django.contrib import admin
from PracticeApp.models import *


# Register your models here.

#admin.site.register(Page)

#admin.register(Page)
#class PageAdmin(admin.ModelAdmin):
#    list_display = ['page_name' , 'page_category','page_publish_date','user']






class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name' , 'department_code']
admin.site.register(Department,DepartmentAdmin)



class StudentAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name'  ,'age' , 'department']
admin.site.register(Student,StudentAdmin)


admin.site.register(Course)

