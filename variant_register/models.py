from django.db import models
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from gene_register.models import Gene


class Variant (models.Model):
    chromosome = models.CharField(max_length=30)
    position = models.IntegerField()
    reference = models.CharField(max_length=30)
    alternative = models.CharField(max_length=30)
    rs = models.CharField(max_length=30)
    gene = models.ForeignKey(Gene, on_delete=models.CASCADE )

    def __str__(self):
        return "CH:"+self.chromosome+" Pos:"+str(self.position)

