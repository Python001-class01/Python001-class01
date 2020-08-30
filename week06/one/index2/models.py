from django.db import models

# Create your models here.
class Movie2(models.Model):
    shorts = models.CharField(max_length=500, blank=True, null=True)
    stars = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie2'