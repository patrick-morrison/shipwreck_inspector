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
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name + " " + self.built + "-" + self.sunk
    

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT, null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    active = models.BooleanField()
    birth_date = models.DateField(null=True, blank=True)
    POSITION_CHOICES = [
        ('ME', 'Member'),
        ('GU', 'Guest'),
        ('AD', 'Admin'),
        ('MU', 'Museum'),
        ('OF', 'Offline'),
    ]
    position = models.CharField(
        max_length=2,
        choices= POSITION_CHOICES,
        default='GUEST',
    )

    def __str__(self):
        return self.first_name + " " + self.last_name

class Report(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    authors = models.ManyToManyField(Person)
    site = models.ForeignKey(Site, on_delete=models.RESTRICT)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    file = models.FileField(upload_to='reports/', null=True, blank=True)

    def __str__(self):
        return self.date.strftime("%Y-%m-%d") + " " + self.site.name + " " + self.title

class Publication(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Person)
    reports = models.ManyToManyField(Report)
    date = models.DateField()
    site = models.ManyToManyField(Site)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    file = models.FileField(upload_to='publications/', null=True, blank=True)

    def __str__(self):
        return self.date.strftime("%Y-%m-%d") + " " + self.title