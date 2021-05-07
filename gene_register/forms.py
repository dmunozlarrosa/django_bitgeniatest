from django import forms
from .models import Gene

class GeneForm(forms.ModelForm):
    class Meta:
        model = Gene
        fields = ("chromosome", "start", "end", "symbol")
        labels = {
            'chromosome':'Cromosoma',
            'start':'Comienzo',
            'end':'Fin',
            'symbol':'Notacion (symbol)',
        }

    def __init__(self, *args, **kwargs):
        super(GeneForm,self).__init__(*args, **kwargs)
class GeneFormList(forms.Form):
    class Meta:
        fields = ("chromosome", "start", "end", "symbol", "rs")
        labels = {
            'chromosome':'Cromosoma',
            'start':'Comienzo',
            'end':'Fin',
            'symbol':'Notacion (symbol)',
            'rs':'Rs.',
        }
    def __init__(self, *args, **kwargs):
        super(GeneFormList,self).__init__(*args, **kwargs)
              
class DiseaseByGeneForm(forms.Form):
    content = forms.CharField()
    class Meta:
        # model = 
        fields = ("chromosome",)
        labels = {
            'chromosome':'Gene (Chormosome) : ',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       