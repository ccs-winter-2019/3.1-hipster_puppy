from django.db import models


class Review(models.Model):
    rating = models.IntegerField(default=5)

