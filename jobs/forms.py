from django import forms

from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['company', 'role', 'applied_date', 'status']
        widgets = {
            'applied_date': forms.DateInput(attrs={'type': 'date'}),
        }
