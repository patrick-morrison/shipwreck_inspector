from django.contrib import admin
from .models import Site, Report, Person, Publication, Project, Photo
from import_export import resources
from import_export.admin import ImportExportModelAdmin

admin.site.register(Person)
admin.site.register(Publication)
admin.site.register(Project)
admin.site.register(Photo)

class SiteResource(resources.ModelResource):

    class Meta:
        model = Site

class SiteAdmin(ImportExportModelAdmin):
    resource_class = SiteResource

admin.site.register(Site, SiteAdmin)

class ReportResource(resources.ModelResource):

    class Meta:
        model = Report

class ReportAdmin(ImportExportModelAdmin):
    resource_class = ReportResource

admin.site.register(Report, ReportAdmin)