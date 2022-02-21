from django.db import models
from django.contrib.auth.models import User

class Site(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    sunk = models.CharField(max_length=255, null=True, blank=True)
    built = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    construction = models.CharField(max_length=255, null=True, blank=True)
    owner = models.CharField(max_length=500, null=True, blank=True)
    size = models.CharField(max_length=500, null=True, blank=True)
    location = models.CharField(max_length=500, null=True, blank=True)
    underwater = models.CharField(max_length=500, null=True, blank=True)
    sinking = models.CharField(max_length=500, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to='hero_images/', null=True, blank=True)
    image_caption = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        if self.sunk is None:
            return self.name
        else:
            return self.name + " (" + self.sunk + ')'

    def last_report(self):
        try:
            return Report.objects.filter(site=self.pk).order_by('-date').first().date
        except:
            return 'never'
    

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

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1200, null=True, blank=True)
    leaders = models.ManyToManyField(Person)
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return self.title

class Report(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    authors = models.ManyToManyField(Person)
    project = models.ManyToManyField(Project, blank=True)
    site = models.ForeignKey(Site, on_delete=models.RESTRICT)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    abstract = models.CharField(max_length=1200, null=True, blank=True)
    file = models.FileField(upload_to='reports/', null=True, blank=True)

    def __str__(self):
        return self.date.strftime("%Y-%m-%d") + " " + self.site.name + " " + self.title

class Publication(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Person)
    project = models.ManyToManyField(Project, blank=True)
    reports = models.ManyToManyField(Report, blank=True)
    date = models.DateField()
    site = models.ManyToManyField(Site)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    abstract = models.CharField(max_length=1200, null=True, blank=True)
    file = models.FileField(upload_to='publications/', null=True, blank=True)

    def __str__(self):
        return self.date.strftime("%Y-%m-%d") + " " + self.title
