from django.db import models

# Create your models here.


class Peak(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=15)
    lat = models.DecimalField(max_digits=25, decimal_places=18)
    long = models.DecimalField(max_digits=25, decimal_places=18)
    #altitude = models.DecimalField(max_length=20)
