from django.db import models
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from gene_register.models import Gene

class Disease (models.Model):
    name = models.CharField(max_length=200, unique=True)
    inheritance = models.BooleanField()

    def __str__(self):
        return self.name

class GeneDisease (models.Model):
    disease =  models.ForeignKey(Disease, on_delete=models.CASCADE)
    gene = models.ForeignKey(Gene, on_delete=models.CASCADE)
    
class DiseaseType (models.Model):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=500)
    
    def __str__(self):
        return self.tipo
