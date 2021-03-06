from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormMixin

from ..models import Report, Site, Photo, Publication

from ..forms import ReportForm, ReportSearch


class reports(FormMixin, generic.ListView):
    model = Report
    paginate_by = 36
    template_name = "sites/reports.html"
    ordering = ['-date']
    form_class = ReportSearch
    def post(self, request, *args, **kwargs):
        form = ReportSearch(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            report = Report.objects.get(id=id)
            return redirect(reverse_lazy('detail_report', kwargs={'pk': report.id}))

class site_reports(generic.ListView):
    paginate_by = 36
    template_name = "sites/site_reports.html"

    def get_queryset(self):
        self.site = get_object_or_404(Site, slug=self.kwargs['slug'])
        return Report.objects.filter(site=self.site)

    def get_context_data(self, **kwargs):
        self.site = get_object_or_404(Site, slug=self.kwargs['slug'])
        self.photos = get_object_or_404(Photo, slug=self.kwargs['slug'])
        context = super().get_context_data(**kwargs)
        reps = Report.objects.filter(site=self.site)
        context['nReports'] = reps.count()
        context['Site'] = self.site

        return context

def CreateReport(request, slug):
    if slug == 'choose_site':
        form = ReportForm(initial={'authors':request.user})
    else:
        Site_id = Site.objects.get(slug=slug)
        form = ReportForm(initial={'authors':request.user,
        'site':Site_id})
    
    if request.method == 'POST':
        filled_form = ReportForm(request.POST, request.FILES)
        if filled_form.is_valid():
            report = Report()
            report.site = filled_form.cleaned_data['site']
            report.title = filled_form.cleaned_data['title']
            report.date = filled_form.cleaned_data['date']
            report.file = filled_form.cleaned_data['file']
            report.abstract = filled_form.cleaned_data['abstract']
            report.user = request.user
            report.save()
            authors = filled_form.cleaned_data['authors']
            report.authors.set(authors)
            projects = filled_form.cleaned_data['project']
            report.project.set(projects)
            report.save()
            return redirect('detail_report', report.pk)

    return render(request, 'sites/create_report.html', {'form': form})

class DetailReport(generic.DetailView):
    model = Report
    template_name = 'sites/detail_report.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        publications = Publication.objects.filter(reports=context['report'])
        context['publications'] = publications
        photos = Photo.objects.filter(report=context['report'])
        context['photos'] = photos
        return context

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
        return reverse_lazy('detail_site', kwargs={'slug': self.object.site.slug})