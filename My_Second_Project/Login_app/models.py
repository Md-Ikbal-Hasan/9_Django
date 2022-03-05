from django.db import models
from django.contrib.auth.models import User  # import User model from django authorization(administration) ........
# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    facebook_id = models.URLField(blank=True)  # blank =True mane chaile ai field ti blank rakhte parbe.....
    profile_pic = models.ImageField(upload_to = 'profile_pics' , blank=True)

    def __Str__(self):
        return self.user.username

