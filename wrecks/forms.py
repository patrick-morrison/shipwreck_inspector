from .models import Publication, Report, Site, Person
from dal import autocomplete
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['title', 'date', 'authors', 'project', 'abstract', 'file',]
        widgets = {
            'date': DateInput,
            'authors': autocomplete.ModelSelect2Multiple(url='person-autocomplete'),
            'project': autocomplete.ModelSelect2Multiple(url='project-autocomplete'),
            'abstract':forms.Textarea,
            }

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['name', 'sunk', 'built', 'owner', 'size', 'location', 'description', 'construction',
              'underwater', 'sinking', 'latitude', 'longitude', 'image', 'image_caption']
        widgets = {
            'underwater':forms.Textarea,
            'sinking':forms.Textarea,
            }

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'date', 'authors', 'site', 'project','reports','abstract',  'file',]
        widgets = {
            'date': DateInput,
            'authors': autocomplete.ModelSelect2Multiple(url='person-autocomplete'),
            'project': autocomplete.ModelSelect2Multiple(url='project-autocomplete'),
            'site': autocomplete.ModelSelect2Multiple(url='site-autocomplete'),
            'reports': autocomplete.ModelSelect2Multiple(url='report-autocomplete'),
            'abstract':forms.Textarea,
            }

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'position', 'user', 'email', 'bio'] 
        widgets = {
            'bio':forms.Textarea,
            'user': autocomplete.ModelSelect2Multiple(url='user-autocomplete'),
            }            
