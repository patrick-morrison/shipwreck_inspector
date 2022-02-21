from django.views import generic
from ..models import Publication
from ..forms import PublicationForm
from django.urls import reverse_lazy

class publications(generic.ListView):
    model = Publication
    paginate_by = 24
    template_name = "meta/publications.html"

class CreatePublications(generic.CreateView):
    model = Publication
    form_class = PublicationForm
    template_name = 'meta/create_publication.html'
    success_url = reverse_lazy('publications')

class DetailPublication(generic.DetailView):
    model = Publication
    template_name = 'meta/detail_publication.html'

class UpdatePublication(generic.UpdateView):
    model = Publication
    template_name = 'meta/update_publication.html'
    form_class = PublicationForm
    def get_success_url(self):
        return reverse_lazy('detail_publication', kwargs={'pk': self.object.pk})

class DeletePublication(generic.DeleteView):
    model = Publication
    template_name = 'sites/delete_publication.html'
    success_url = reverse_lazy('publications')