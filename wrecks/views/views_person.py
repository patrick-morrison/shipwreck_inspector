from django.views import generic
from django.shortcuts import redirect, render
from ..models import Person, Report, Publication, Project
from ..forms import PersonForm, PersonSearch
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin

class persons(FormMixin, generic.ListView):
    model = Person
    paginate_by = 36
    template_name = "meta/people.html"
    form_class = PersonSearch
    def post(self, request, *args, **kwargs):
        form = PersonSearch(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            person = Person.objects.get(id=id)
            return redirect(reverse_lazy('detail_person', kwargs={'pk': person.id}))

class CreatePerson(generic.CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'meta/create_person.html'
    def get_success_url(self):
        return reverse_lazy('detail_person', kwargs={'pk': self.object.pk})

class DetailPerson(generic.DetailView):
    model = Person
    template_name = 'meta/detail_person.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reports = Report.objects.filter(authors=context['person'])
        context['reports'] = reports
        context['publications'] = Publication.objects.filter(authors=context['person']).distinct()
        context['projects_lead'] = Project.objects.filter(leaders=context['person']).distinct()
        context['projects'] = Project.objects.filter(report__in=reports).distinct()
        return context

class UpdatePerson(generic.UpdateView):
    model = Person
    template_name = 'meta/update_person.html'
    form_class = PersonForm
    def get_success_url(self):
        return reverse_lazy('detail_person', kwargs={'pk': self.object.pk})

class DeletePerson(generic.DeleteView):
    model = Person
    template_name = 'meta/delete_person.html'
    success_url = reverse_lazy('people')