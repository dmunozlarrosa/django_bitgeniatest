from django import forms
from .models import Variant


class VariantForm(forms.ModelForm):

    class Meta:
        model = Variant
        fields = ('chromosome', 'position', 'reference','alternative', 'rs', 'gene')
        # fields = ('chromosome', 'position', 'reference','alternative', 'rs', 'gene.id')
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
