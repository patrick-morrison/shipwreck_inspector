from django.views import generic
from ..models import Person
from ..forms import PersonForm
from django.urls import reverse_lazy
from django.shortcuts import redirect, render

class persons(generic.ListView):
    model = Person
    paginate_by = 24
    template_name = "meta/people.html"

class CreatePerson(generic.CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'meta/create_person.html'
    success_url = reverse_lazy('home')