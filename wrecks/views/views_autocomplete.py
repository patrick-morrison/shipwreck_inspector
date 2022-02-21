from ..models import Person, Site, Report, Project
from dal import autocomplete

class PersonAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Person.objects.none()

        qs = Person.objects.all()

        if self.q:
            qs = qs.filter(first_name__icontains=self.q) | qs.filter(last_name__icontains=self.q)

        return qs

class ProjectAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Project.objects.none()

        qs = Project.objects.all()

        if self.q:
            qs = qs.filter(title__icontains=self.q) | qs.filter(description__icontains=self.q)

        return qs

class SiteAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Site.objects.none()

        qs = Site.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q) | qs.filter(sunk__icontains=self.q) | qs.filter(built__icontains=self.q) | qs.filter(description__icontains=self.q)| qs.filter(construction__icontains=self.q)

        return qs

class ReportAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Report.objects.none()

        qs = Report.objects.all()

        if self.q:
            qs = qs.filter(title__icontains=self.q) | qs.filter(date__icontains=self.q) | qs.filter(site__name__icontains=self.q)

        return qs