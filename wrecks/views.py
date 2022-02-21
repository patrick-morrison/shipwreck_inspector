from pipes import Template
from re import template
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Report, Site, Person, Project

from .forms import ReportForm, SiteForm
from dal import autocomplete



# Create your views here.

def home(request):
    return render(request, 'wrecks/home.html')


class sites(generic.ListView):
    model = Site
    paginate_by = 12
    template_name = "sites/sites.html"

class reports(generic.ListView):
    model = Report
    paginate_by = 24
    template_name = "sites/reports.html"

class site_reports(generic.ListView):
    paginate_by = 20
    template_name = "sites/site_reports.html"

    def get_queryset(self):
        self.site = get_object_or_404(Site, id=self.kwargs['pk'])
        return Report.objects.filter(site=self.site).order_by('-date')

    def get_context_data(self, **kwargs):
        self.site = get_object_or_404(Site, id=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        reps = Report.objects.filter(site=self.site)
        context['nReports'] = reps.count()
        context['Site'] = self.site

        return context


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = "registration/signup.html"

    def form_valid(self, form):
        view = super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get(
            'username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view


class CreateSite(generic.CreateView):
    model = Site
    form_class = SiteForm
    template_name = 'sites/create_site.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(CreateSite, self).form_valid(form)
        return redirect(reverse_lazy('detail_site', kwargs={'pk': self.object.pk}))


class DetailSite(generic.DetailView):
    model = Site
    template_name = 'sites/detail_site.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reps = Report.objects.filter(site=context['site'])
        reps_filtered = reps.order_by('-date')[0:10]
        context['Reports'] = reps_filtered
        context['nReports'] = reps.count()
        context['nReportsDisp'] = reps_filtered.count()
        return context


class UpdateSite(generic.UpdateView):
    model = Site
    template_name = 'sites/update_site.html'
    form_class = SiteForm

    def get_success_url(self):
        return reverse_lazy('detail_site', kwargs={'pk': self.object.pk})


class DeleteSite(generic.DeleteView):
    model = Site
    template_name = 'sites/delete_site.html'
    success_url = reverse_lazy('sites')

# class CreateReport(generic.CreateView):
#    model = Report
#    fields = ['title', 'authors', 'date', 'site']
#    template_name = 'sites/create_report.html'
#    success_url = reverse_lazy('home')

#    def form_valid(self, form):
#        form.instance.user = self.request.user
#        super(CreateReport, self).form_valid(form)
#        return redirect('home')


def CreateReport(request, pk):
    form = ReportForm()

    Site_id = Site.objects.get(pk=pk)

    if request.method == 'POST':
        filled_form = ReportForm(request.POST, request.FILES)
        if filled_form.is_valid():
            report = Report()
            report.title = filled_form.cleaned_data['title']
            report.date = filled_form.cleaned_data['date']
            report.file = filled_form.cleaned_data['file']
            report.site = Site.objects.get(pk=pk)
            report.user = request.user
            report.save()
            authors = filled_form.cleaned_data['authors']
            report.authors.set(authors)
            report.save()
            return redirect('detail_site', pk)

    return render(request, 'sites/create_report.html', {'form': form, 'site':Site_id})

class DetailReport(generic.DetailView):
    model = Report
    template_name = 'sites/detail_report.html'

class UpdateReport(generic.UpdateView):
    model = Report
    template_name = 'sites/update_report.html'
    form_class = ReportForm
    def get_success_url(self):
        return reverse_lazy('detail_report', kwargs={'pk': self.object.pk})

class DeleteReport(generic.DeleteView):
    model = Report
    template_name = 'sites/delete_report.html'
    def get_success_url(self):
        return reverse_lazy('detail_site', kwargs={'pk': self.object.site.pk})

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