from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import generic

from ..models import Report, Site, Photo

from ..forms import ReportForm


class reports(generic.ListView):
    model = Report
    paginate_by = 24
    template_name = "sites/reports.html"
    ordering = ['-date']

class site_reports(generic.ListView):
    paginate_by = 20
    template_name = "sites/site_reports.html"

    def get_queryset(self):
        self.site = get_object_or_404(Site, id=self.kwargs['pk'])
        return Report.objects.filter(site=self.site)

    def get_context_data(self, **kwargs):
        self.site = get_object_or_404(Site, id=self.kwargs['pk'])
        self.photos = get_object_or_404(Photo, id=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        reps = Report.objects.filter(site=self.site)
        context['nReports'] = reps.count()
        context['Site'] = self.site

        return context

def CreateReport(request, pk):
    form = ReportForm(initial={'authors':request.user})

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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
        return reverse_lazy('detail_site', kwargs={'pk': self.object.site.pk})