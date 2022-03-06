from django import forms
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from ..forms import PreferencesForm
from ..models import Person


def home(request):
    return(redirect(reverse_lazy('sites')))

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = "registration/signup.html"

    def form_valid(self, form):
        view = super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get(
            'username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view

def preferences(request):
    form = PreferencesForm
    user = get_object_or_404(User, pk=request.user.pk)
    person = get_object_or_404(Person, user=request.user)
    if request.method == 'POST':
        filled_form = PreferencesForm(request.POST, instance=user)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('preferences')
    return render(request, 'registration/preferences.html',
     {'user': request.user, 'person' : person,
     'form' : form(initial={'email': user.email,
     'username':user.username,
     'person': person},)
    })
    