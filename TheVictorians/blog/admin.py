from django.contrib import admin
from blog.models import Blog
# Register your models here.



class BlogAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all" : ("css/",)
        }
        js = ("js/blog.js",)

admin.site.register(Blog , BlogAdmin)

