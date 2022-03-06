from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, models


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
    form = UserChangeForm
    if request.method == 'POST':
        filled_form = UserChangeForm(request.POST, instance=request.user)
        if filled_form.is_valid():
            user = request.user
            user.email = filled_form.cleaned_data['email1']
            user.save()
            return redirect('preferences')
    return render(request, 'registration/preferences.html',
     {'user': request.user,
     'form' : form(initial={'email': request.user.email,
     'username':request.user.username },)
    })
    