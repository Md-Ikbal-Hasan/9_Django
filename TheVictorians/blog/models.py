from django.db import models

# Create your models here.
class Blog(models.Model):
    sno = models.AutoField(primary_key=True)   # since it was not migrate ,thats why I define it as primary key
    title = models.CharField(max_length = 200)
    content  = models.TextField()
    slug = models.CharField(max_length = 100)
    time = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.title