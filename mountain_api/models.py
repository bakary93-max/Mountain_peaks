from django.db import models

# Create your models here.


class Peak(models.Model):
    name = models.CharField(max_length=15)
    lat = models.DecimalField(max_length=20)
    long = models.DecimalField(max_length=20)
    altitude = models.DecimalField(max_length=20)
