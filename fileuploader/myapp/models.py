from django.db import models


# Create your models here.

class Candidate(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    job_title = models.CharField(max_length=20)
    applicants_cv = models.FileField(upload_to='applicants_cv')

    def __str__(self):
        return self.name


    
