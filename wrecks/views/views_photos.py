from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy

from ..models import Report, Photo

from ..forms import PhotoForm, PhotoFormSingle

def CreatePhoto(request, pk):

    Report_id = Report.objects.get(pk=pk)
    form = PhotoForm(initial={'date': Report_id.date, 'authors':request.user})

    if request.method == 'POST':
        filled_form = PhotoForm(request.POST, request.FILES)
        if filled_form.is_valid():
            files = request.FILES.getlist('file')
            for f in files:
                photo = Photo()
                photo.caption = filled_form.cleaned_data['caption']
                photo.date = filled_form.cleaned_data['date']
                photo.file = f
                photo.report = Report.objects.get(pk=pk)
                photo.user = request.user
                photo.save()
                photo.authors.set(filled_form.cleaned_data['authors'])
                photo.save()
            return redirect('detail_report', pk)

    return render(request, 'sites/create_photo.html', {'form': form, 'report':Report_id})

class UpdatePhoto(generic.UpdateView):
    model = Photo
    template_name = 'sites/update_photo.html'
    form_class = PhotoFormSingle
    def get_success_url(self):
        return reverse_lazy('detail_report', kwargs={'pk': self.object.report.pk})

class DeletePhoto(generic.DeleteView):
    model = Photo
    template_name = 'sites/delete_photo.html'
    def get_success_url(self):
        return reverse_lazy('detail_report', kwargs={'pk': self.object.report.pk})