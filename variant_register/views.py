from django.shortcuts import render, redirect
from .forms import VariantForm
from .models import Variant
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from gene_register.models import Gene
from django.contrib.auth.decorators import login_required

@login_required
def variant_list(request):
    context = {'variant_list': Variant.objects.all()}
    return render(request, "variant_register/variant_list.html", context)

@login_required
def variant_form(request, id=0):
    print("request")
    print(request)
    if request.method == "GET":
        if id == 0:
            form = VariantForm()
        else:
            v = Variant.objects.get(pk=id)
            form = VariantForm(instance=v)
            symbol = v.gene.symbol
        return render(request, "variant_register/variant_form.html", {'form': form})
    else:
        if id == 0:
            form = VariantForm(request.POST)
        else:
            v = Variant.objects.get(pk=id)
            form = VariantForm(request.POST, instance=v)
        if form.is_valid():
            form.save()
        return redirect('/variant/list')

@login_required
def variant_delete(request, id):
    variant = Variant.objects.get(pk=id)
    variant.delete()
    return redirect('/variant/list')
