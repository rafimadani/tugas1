from django.db import models

# Create your models here.
class moviesitem(models.Model):
    watched = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    rating = models.CharField(max_length=5)
    release_date = models.CharField(max_length=50)
    review = models.TextField()
