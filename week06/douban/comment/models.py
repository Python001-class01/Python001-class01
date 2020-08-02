from django.db import models

# Create your models here.
class MovieInfo(models.Model):
    comment = models.CharField(max_length=500)
    rate = models.IntegerField(default=0)