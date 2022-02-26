from .models import Publication, Report, Site, Person, Photo
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
            'abstract':forms.Textarea(attrs={'cols': 30, 'rows': 8}),
            }

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['name', 'sunk', 'built', 'description', 'construction', 'size', 'owner', 'built_details',  
              'sinking', 'underwater', 'location', 'region', 'latitude', 'longitude',  'image', 'image_caption', 'sketchfab_link', 'museum_link', 'dave_link']
        widgets = {
            'description':forms.TextInput,
            'owner':forms.TextInput,
            'construction':forms.TextInput,
            'size':forms.TextInput,
            'built_details':forms.Textarea(attrs={'cols': 30, 'rows': 4}),
            'sinking':forms.Textarea(attrs={'cols': 30, 'rows': 4}),
            'underwater':forms.Textarea(attrs={'cols': 30, 'rows': 4}),
            'location':forms.Textarea(attrs={'cols': 30, 'rows': 4}),
            'image_caption':forms.Textarea(attrs={'cols': 30, 'rows': 2}),
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
            'abstract':forms.Textarea(attrs={'cols': 30, 'rows': 12}),
            }

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'position', 'user', 'email', 'bio'] 
        widgets = {
            'bio':forms.Textarea,
            'user': autocomplete.ModelSelect2Multiple(url='user-autocomplete'),
            }            

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['caption', 'date', 'authors', 'file']
        widgets = {
            'date': DateInput,
            'authors': autocomplete.ModelSelect2Multiple(url='person-autocomplete'),
            'file':forms.ClearableFileInput(attrs={'multiple': True}),
            'caption':forms.TextInput,
            }

class PhotoFormSingle(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['caption', 'date', 'authors', 'file']
        widgets = {
            'date': DateInput,
            'authors': autocomplete.ModelSelect2Multiple(url='person-autocomplete'),
            'caption':forms.TextInput,
            }

class SiteSearch(forms.Form):
        id = forms.CharField(widget=autocomplete.ListSelect2(
            url='site-autocomplete',
            attrs={'data-placeholder': 'Search', 'dropdownAutoWidth':'false',
    },))