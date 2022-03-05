from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Department(models.Model):
    name  = models.CharField(max_length=20)
    department_code = models.IntegerField()

    def __str__(self):
        return str(self.name)

    
class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    department = models.ForeignKey(Department , on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Course(models.Model):
    name = models.CharField(max_length=30)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return str(self.name)

  







