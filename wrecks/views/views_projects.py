from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormMixin

from ..models import Project, Report, Publication

from ..forms import ProjectForm, ProjectSearch

class projects(FormMixin, generic.ListView):
    model = Project
    paginate_by = 24
    template_name = "meta/projects.html"
    form_class = ProjectSearch
    def post(self, request, *args, **kwargs):
        form = ProjectSearch(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            project = Project.objects.get(id=id)
            return redirect(reverse_lazy('detail_project', kwargs={'slug': project.slug}))

def CreateProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        filled_form = ProjectForm(request.POST, request.FILES)
        if filled_form.is_valid():
            project = Project()
            project.title = filled_form.cleaned_data['title']
            project.slug = filled_form.cleaned_data['slug']
            project.description = filled_form.cleaned_data['description']
            project.date_start = filled_form.cleaned_data['date_start']
            project.date_end = filled_form.cleaned_data['date_end']
            project.save()
            project.leaders.set(filled_form.cleaned_data['leaders'])
            project.save()
            return redirect('detail_project', project.slug)

    return render(request, 'meta/create_project.html', {'form': form})

class DetailProject(generic.DetailView):
    model = Project
    template_name = 'meta/detail_project.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reps = Report.objects.filter(project=context['project'])
        reps_filtered = reps[0:10]
        context['Reports'] = reps_filtered
        context['nReports'] = reps.count()
        context['nReportsDisp'] = reps_filtered.count()
        pubs = Publication.objects.filter(project=context['project'])
        context['Publications'] = pubs
        return context
    

class UpdateProject(generic.UpdateView):
    model = Project
    template_name = 'meta/update_project.html'
    form_class = ProjectForm
    def get_success_url(self):
        return reverse_lazy('detail_project', kwargs={'slug': self.object.slug})

class DeleteProject(generic.DeleteView):
    model = Project
    template_name = 'meta/delete_project.html'
    success_url = reverse_lazy('projects')