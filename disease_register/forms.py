from django import forms
from .models import Disease
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from gene_register.models import Gene


class DiseaseForm(forms.ModelForm):
    class Meta:
        model = Disease
        # fields = ("name", "inheritance", "genedisease")
        fields = ("name", "inheritance")
        labels = {
            'name': 'Enfermedad',
            'inheritance': 'Herencia',
            # 'gene': 'Gene'
        }
        # gene = forms.ModelMultipleChoiceField(queryset=Gene.objects.all())

    def __init__(self, *args, **kwargs):
        super(DiseaseForm, self).__init__(*args, **kwargs)
