from django.db import models

# Create your models here.

class StudentDetails(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    class_name = models.IntegerField()
    result = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return str(self.name)

