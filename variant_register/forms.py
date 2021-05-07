from django import forms
from .models import Variant
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from gene_register.models import Gene

class VariantForm(forms.ModelForm):

    class Meta:
        model = Variant
        fields = ('chromosome', 'position', 'reference','alternative', 'rs', 'gene')
        labels = {
            'chromosome': 'Cromosoma',
            'position': 'Posicion',
            'reference': 'Referencia',
            'alternative': 'Alternativa',
            'rs': 'Rs.',
            'gene': 'Gen'
        }
        

    def __init__(self, *args, **kwargs):
        super(VariantForm, self).__init__(*args, **kwargs)
        # forms.ModelChoiceField(to_field_name='id')
