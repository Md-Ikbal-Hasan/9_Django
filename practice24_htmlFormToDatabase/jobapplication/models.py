from django.db import models

# Create your models here.
class ApplicantsInfo(models.Model):
    name = models.CharField(max_length=30,null=False,blank=False)
    email = models.EmailField(null=False,blank=False)
    birthday = models.DateField(null=False,blank=False)
    job_position = models.CharField(max_length=30,null=False,blank=False)
    gender = models.CharField(max_length=20,null=False,blank=False)
    interest = models.CharField(max_length=300,null=True,default=None)
    cover_letter = models.TextField(null=False,blank=False)
    cv = models.FileField(upload_to='cv', max_length=250, default=None)


    def __str__(self):
        return self.email


class RefferelForm(models.Model):
    pass
