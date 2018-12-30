import datetime

from django.db import models
from django.utils import timezone


# Create your models here.


class Poids(models.Model):
    poids = models.IntegerField()

    date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def getPoidsDansIntervalle(self,date_debut,date_fin):
        return Poids.objects.filter(date__lt=date_fin,date__gte=date_debut)
