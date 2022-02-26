from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormMixin

from ..models import Publication, Report, Site

from ..forms import SiteForm, SiteSearch

class sites(FormMixin, generic.ListView):
    model = Site
    paginate_by = 24
    template_name = "sites/sites.html"
    form_class = SiteSearch
    def post(self, request, *args, **kwargs):
        form = SiteSearch(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            site = Site.objects.get(id=id)
            return redirect(reverse_lazy('detail_site', kwargs={'slug': site.slug}))


def sites_map(request):
    return render(request, 'sites/sites_map.html')

class CreateSite(generic.CreateView):
    model = Site
    form_class = SiteForm
    template_name = 'sites/create_site.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(CreateSite, self).form_valid(form)
        return redirect(reverse_lazy('detail_site', kwargs={'slug': self.object.slug}))


class DetailSite(generic.DetailView):
    model = Site
    template_name = 'sites/detail_site.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reps = Report.objects.filter(site=context['site'])
        reps_filtered = reps[0:10]
        context['Reports'] = reps_filtered
        context['nReports'] = reps.count()
        context['nReportsDisp'] = reps_filtered.count()
        pubs = Publication.objects.filter(site=context['site'])
        context['Publications'] = pubs
        return context


class UpdateSite(generic.UpdateView):
    model = Site
    template_name = 'sites/update_site.html'
    form_class = SiteForm

    def get_success_url(self):
        return reverse_lazy('detail_site', kwargs={'slug': self.object.slug})


class DeleteSite(generic.DeleteView):
    model = Site
    template_name = 'sites/delete_site.html'
    success_url = reverse_lazy('sites')