from django.contrib import admin
from .models import Site, Report, Person, Publication, Project, Photo
from import_export import resources
from import_export.admin import ImportExportModelAdmin

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

class PersonResource(resources.ModelResource):

    class Meta:
        model = Person

class PersonAdmin(ImportExportModelAdmin):
    resource_class = PersonResource

admin.site.register(Person, PersonAdmin)


class PublicationResource(resources.ModelResource):

    class Meta:
        model = Publication

class PublicationAdmin(ImportExportModelAdmin):
    resource_class = PublicationResource

admin.site.register(Publication, PublicationAdmin)

class ProjectResource(resources.ModelResource):

    class Meta:
        model = Project

class ProjectAdmin(ImportExportModelAdmin):
    resource_class = ProjectResource

admin.site.register(Project, ProjectAdmin)

class PhotoResource(resources.ModelResource):

    class Meta:
        model = Photo

class PhotoAdmin(ImportExportModelAdmin):
    resource_class = PhotoResource

admin.site.register(Photo, PhotoAdmin)