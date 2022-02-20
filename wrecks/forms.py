from .models import Report, Site
from dal import autocomplete
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['title', 'date', 'authors', 'file']
        widgets = {
            'date': DateInput,
            'authors': autocomplete.ModelSelect2Multiple(url='person-autocomplete'),
            }

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['name', 'sunk', 'built', 'owner', 'size', 'location',
              'underwater', 'sinking', 'latitude', 'longitude', 'image', 'image_caption']
        widgets = {
            'underwater':forms.Textarea,
            'sinking':forms.Textarea,
            }