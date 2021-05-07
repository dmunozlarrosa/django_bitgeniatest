from gene_register.models import Gene
from variant_register.models import Variant
from disease_register.models import Disease, GeneDisease, DiseaseType
import csv
import os
path = os.path.abspath(os.getcwd()) + "\data\\"
with open(path + 'Gene.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        g = Gene(
            id=row['id'],
            symbol=row['symbol'],
            chromosome=row['chromosome'],
            start=row['start'],
            end=row['end'])
        g.save()
    print("* Gene    DB table filled")
with open(path + 'Variant.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        v = Variant(
            gene=Gene.objects.get(id=row['gene']),
            chromosome=row['chromosome'],
            position=row['position'],
            rs=row['rs'],
            reference=row['reference'],
            alternative=row['alternative'])
        v.save()
    print("* Variant DB table filled")

with open(path + 'Disease.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        d = Disease(
            id=row['id'],
            name=row['name'],
            inheritance=row['inheritance'])
        d.save()
    print("* Disease DB table filled")

with open(path + 'DiseaseType.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dt = DiseaseType(
            id=row['id'],
            disease=Disease.objects.get(id=row['disease']),
            tipo=row['tipo'])
        dt.save()
    print("* DiseaseType DB table filled")

with open(path + 'GeneDisease.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        gd = GeneDisease(
            id=row['id'],
            gene=Gene.objects.get(id=row['gene']),
            disease=Disease.objects.get(id=row['disease']))
        gd.save()
    print("* GeneDisease DB table filled")

# Run populator with:
#                      py manage.py shell
#                      exec(open('populator.py').read())
