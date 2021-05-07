from django.shortcuts import render, redirect
from .forms import DiseaseForm
from .models import Disease, GeneDisease, DiseaseType
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from gene_register.models import Gene
from django.contrib.auth.decorators import login_required

@login_required
def disease_list(request):
    context = {'disease_list': Disease.objects.all()}
    return render(request, "disease_register/disease_list.html", context)

@login_required
def disease_form(request, id=0):
    print("request")
    print(request)
    if request.method == "GET":
        if id == 0:
            form = DiseaseForm()
        else:
            d = Disease.objects.get(pk=id)
            gene_disease_list = []
            for y in GeneDisease.objects.values(): 
                if y['disease_id'] == d.id :
                    gene_disease_list.append(y['gene_id'])
            gene_list = []
            for y in Gene.objects.values(): 
                if y['id'] in gene_disease_list :
                    gene_list.append(y['symbol'])
            form = DiseaseForm(instance=d)
            disease_tipo = []
            print("disease_tipo")
            for y in DiseaseType.objects.values(): 
                if y['disease_id'] == d.id : 
                    disease_tipo.append(y['tipo']) 
            print("disease_tipo")
            print(disease_tipo)
        return render(request, "disease_register/disease_form.html", {
            'form': form,
            'gene_list': gene_list,
            'disease_tipo' : disease_tipo,
        })
    else:
        if id == 0:
            form = DiseaseForm(request.POST)
        else:
            d = Disease.objects.get(pk=id)
            form = DiseaseForm(request.POST, instance=d)
        if form.is_valid():
            form.save()
        return redirect('/disease/list')

@login_required
def disease_delete(request, id):
    disease = Disease.objects.get(pk=id)
    disease.delete()
    return redirect('/disease/list')
