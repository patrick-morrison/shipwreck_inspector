from ..models import Person, Site, Report, Project, Publication
from django.contrib.auth.models import User
from dal import autocomplete

class PersonAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        qs = Person.objects.all()

        if self.q:
            qs = qs.filter(first_name__icontains=self.q) | qs.filter(last_name__icontains=self.q)

        return qs

class ProjectAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        qs = Project.objects.all()

        if self.q:
            qs = qs.filter(title__icontains=self.q) | qs.filter(description__icontains=self.q)

        return qs

class SiteAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        qs = Site.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q) | qs.filter(sunk__icontains=self.q) | qs.filter(built__icontains=self.q) | qs.filter(description__icontains=self.q)| qs.filter(construction__icontains=self.q)

        return qs

class ReportAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        qs = Report.objects.all()

        if self.q:
            qs = qs.filter(title__icontains=self.q) | qs.filter(date__icontains=self.q) | qs.filter(site__name__icontains=self.q)

        return qs

class UserAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        qs = User.objects.all()

        if self.q:
            qs = qs.filter(firstname__icontains=self.q) | qs.filter(lastname__icontains=self.q)

        return qs

class PublicationAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Publication.objects.none()

        qs = Publication.objects.all()

        if self.q:
            qs = qs.filter(title__icontains=self.q) | qs.filter(date__icontains=self.q) | qs.filter(abstract__icontains=self.q)

        return qs