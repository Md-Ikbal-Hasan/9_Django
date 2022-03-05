from django.contrib import admin
from .models import Blog
# Register your models here.


""" 
@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','desc']
""" 



class BlogAdmin(admin.ModelAdmin):
    list_display = ['title' , 'desc']
admin.site.register(Blog,BlogAdmin)


