from django.views import generic
from ..models import Publication
from ..forms import PublicationForm
from django.urls import reverse_lazy
from django.shortcuts import redirect, render

class publications(generic.ListView):
    model = Publication
    paginate_by = 24
    template_name = "meta/publications.html"

def CreatePublication(request):
    form = PublicationForm()

    if request.method == 'POST':
        filled_form = PublicationForm(request.POST, request.FILES)
        if filled_form.is_valid():
            pub = Publication()
            pub.title = filled_form.cleaned_data['title']
            pub.date = filled_form.cleaned_data['date']
            pub.abstract = filled_form.cleaned_data['abstract']
            pub.user = request.user
            pub.file = filled_form.cleaned_data['file']
            pub.save()
            pub.site.set(filled_form.cleaned_data['site'])
            pub.authors.set(filled_form.cleaned_data['authors'])
            pub.project.set(filled_form.cleaned_data['project'])
            pub.report.set(filled_form.cleaned_data['report'])
            pub.save()
            return redirect('detail_publication', pub.pk)

    return render(request, 'meta/create_publication.html', {'form': form})

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
    template_name = 'meta/delete_publication.html'
    success_url = reverse_lazy('publications')