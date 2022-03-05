from django.db import models

# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length=50)
    taskDesc = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.taskTitle



class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    desc = models.TextField()

    def __str__(self):
        return self.name