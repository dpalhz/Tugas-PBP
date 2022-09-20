from django.db import models

# Create your models here.
class FilmItem(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=30)
    rating = models.IntegerField()
    release_date = models.CharField(max_length=30)
    review = models.TextField()
   