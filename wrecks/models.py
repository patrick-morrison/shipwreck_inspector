from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class Site(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    sunk = models.CharField(max_length=255)
    built = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    construction = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    underwater = models.CharField(max_length=255)
    sinking = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=19, decimal_places=10)
    longitude = models.DecimalField(max_digits=19, decimal_places=10)

class Report(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    site = models.ForeignKey(Site, on_delete=models.RESTRICT)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)