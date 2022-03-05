from django.db import models

# Create your models here.


class User(models.Model):        # User is a table name of database. In Django database there will be create a table named User.......
    name  =models.CharField(max_length=30)    # name , emai, password are attribute of User table .........
    email  =models.EmailField(max_length=100)
    password  =models.CharField(max_length=100)
   
