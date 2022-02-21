from django.contrib import admin
from .models import Site, Report, Person, Publication, Project

admin.site.register(Site)
admin.site.register(Report)
admin.site.register(Person)
admin.site.register(Publication)
admin.site.register(Project)