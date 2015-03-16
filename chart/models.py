from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Country(models.Model):
    region = models.ForeignKey(Region)
    name = models.CharField(max_length=50, unique=True)
    value = models.FloatField()