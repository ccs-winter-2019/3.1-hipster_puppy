from django.db import models


class Album(models.Model):
    pass


class Photo(models.Model):
    title = models.CharField(max_length=255)
    picture = models.URLField()
    description = models.TextField(null=True)


kepler = Photo()
oz = Photo()

photos = [kepler, oz]