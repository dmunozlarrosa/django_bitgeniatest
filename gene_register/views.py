from django.shortcuts import render, redirect
from .forms import GeneForm, GeneFormList, DiseaseByGeneForm
from .models import Gene
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from variant_register.models import Variant
from disease_register.models import Disease, DiseaseType, GeneDisease
from django.contrib.auth.decorators import login_required

@login_required
def gene_list(request):
    print("gene_list")
    newGeneList = Gene.objects.values()
    for i,x in enumerate(newGeneList):
        rslist = ""
        for y in Variant.objects.values(): 
            if y['gene_id'] == x['id'] : 
                comma = "" if rslist == "" else ", "
                rslist += comma + y['rs'] 
        newGeneList[i]['rs'] = rslist
    return render(request, "gene_register/gene_list.html", {
        'gene_list': newGeneList, 
    })

@login_required
def gene_form(request, id=0):
    print("gene_form")
    if request.method == "GET":
        disease_list = []
        gene_disease_list = []
        variant_list = ""
        if id == 0:
            form = GeneForm()
            return render(request, "gene_register/gene_form.html", {'form': form})
        else:
            g = Gene.objects.get(pk=id)
            form = GeneForm(instance=g)
            for y in GeneDisease.objects.values(): 
                if y['gene_id'] == g.id :
                    gene_disease_list.append(y['disease_id'])
            for y in Disease.objects.values(): 
                if y['id'] in gene_disease_list :
                    disease_list.append(y['name'])
            for y in Variant.objects.values(): 
                if y['gene_id'] == g.id : 
                    comma = "" if variant_list == "" else ", "
                    variant_list += comma + y['rs'] 
        return render(request, "gene_register/gene_form.html", {
            'form': form,
            'disease_list' : disease_list,
            'variant_list' : variant_list,
        })
    else:
        print("Aaaaaa")
        if id == 0:
            form = GeneFormList(request.POST)
        else:
            g = Gene.objects.get(pk=id)
            form = GeneForm(request.POST, instance=g)
        if form.is_valid():
            form.save()
        return redirect('/gene/list')
# DiseaseByGene

@login_required
def gene_delete(request, id):
    gene = Gene.objects.get(pk=id)
    gene.delete()
    return redirect('/gene/list')
