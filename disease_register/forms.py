from django import forms
from .models import Disease


class DiseaseForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = ("name", "inheritance")
        labels = {
            'name': 'Enfermedad',
            'inheritance': 'Herencia',
            # 'gene': 'Gene'
        }

    def __init__(self, *args, **kwargs):
        super(DiseaseForm, self).__init__(*args, **kwargs)
