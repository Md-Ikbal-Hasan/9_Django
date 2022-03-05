from django.db import models

# Create your models here.

class Musician(models.Model):    # musician is a table name........
    # id = models.AutoField(primary_key=True) # this is automaticlly added in hiden ........
    first_name = models.CharField(max_length = 50 , null=True)
    last_name = models.CharField(max_length = 50)
    instrument = models.CharField(max_length = 100)

    def __str__(self):
        return str(self.first_name) + " " +  str(self.last_name)
        


class Album(models.Model):     #Album is a table name.........
    # id = models.AutoField(primary_key=True)
    artist = models.ForeignKey(Musician , on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()

    # tuple
    rating = (
        (1,"Worstttt"),
        (2,"Bad"),
        (3,"Not Bad"),
        (4,"Good"),
        (5,"Excellent!"),
    )

    num_stars = models.IntegerField(choices=rating)


    def __str__(self):
        return str(self.name) + " , Rating:  " + str(self.num_stars)
