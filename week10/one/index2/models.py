from django.db import models

# Create your models here.


class Movie2(models.Model):
    shorts = models.CharField(max_length=500, blank=True, null=True)
    stars = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie2'


class Zdm_pro_com(models.Model):
    comment = models.CharField(max_length=5000, blank=True, null=True)
    band = models.CharField(max_length=50, blank=True, null=True)
    #id  = models.IntegerField(blank=True, null=True)
    shijian = models.CharField(max_length=500, blank=True, null=True)
    shoujiming2 = models.CharField(max_length=500, blank=True, null=True)
    sentiment = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zdm_pro_com3'
