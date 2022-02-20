from django.contrib import admin
from .models import Site, Report, Person, Publication

admin.site.register(Site)
admin.site.register(Report)
admin.site.register(Person)
admin.site.register(Publication)