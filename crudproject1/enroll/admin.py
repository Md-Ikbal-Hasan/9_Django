from django.contrib import admin
#from enroll.models import User     # imported one model from models
from enroll.models import *         # all models from models imported here.....


# Register your models here.

#admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id'  , 'name' , 'email' , 'password')