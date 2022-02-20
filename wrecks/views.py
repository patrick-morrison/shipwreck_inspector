from pipes import Template
from re import template
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Report, Site


# Create your views here.

def home(request):
    return render(request, 'wrecks/home.html')

class sites(generic.ListView):
    model = Site
    paginate_by = 8
    template_name = "sites/sites.html"


def reports(request):
    return render(request, 'sites/reports.html')

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = "registration/signup.html"

    def form_valid(self, form):
        view = super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get('username'),form.cleaned_data.get('password1')
        user = authenticate(username = username, password = password)
        login(self.request, user)
        return view


class CreateSite(generic.CreateView):
    model = Site
    fields = ['name', 'sunk', 'built', 'owner', 'size', 'location', 'underwater', 'sinking', 'latitude', 'longitude']
    template_name = 'sites/create_site.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(CreateSite, self).form_valid(form)
        return redirect('home')


class DetailSite(generic.DeleteView):
    model = Site
    template_name = 'sites/detail_site.html'

class UpdateSite(generic.UpdateView):
    model = Site
    template_name = 'sites/update_site.html'
    fields = ['name', 'sunk', 'built', 'owner', 'size', 'location', 'underwater', 'sinking', 'latitude', 'longitude']
    success_url = reverse_lazy('sites')

class DeleteSite(generic.DeleteView):
    model = Site
    template_name = 'sites/delete_site.html'
    success_url = reverse_lazy('sites')

class CreateReport(generic.CreateView):
    model = Report
    fields = ['title', 'date', 'site']
    template_name = 'sites/create_report.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(CreateReport, self).form_valid(form)
        return redirect('home')