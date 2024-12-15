from django import forms
from .models import PoliceReport

class PoliceReportForm(forms.ModelForm):
    class Meta:
        model = PoliceReport
        fields = ['incident_type', 'location', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }
