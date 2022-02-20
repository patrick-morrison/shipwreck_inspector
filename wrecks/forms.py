from .models import Report
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

