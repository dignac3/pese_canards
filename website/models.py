import csv
import datetime
import json
import os
from os.path import exists

from django.core.files import File
from django.db import models
from django.utils import timezone

# Create your models here.





class Pesee(models.Model):

    id = models.AutoField(primary_key=True)
    semaine = models.IntegerField()
    poids_min = models.IntegerField()
    poids_max = models.IntegerField()
    tare = models.IntegerField()

    date_debut = models.DateTimeField(auto_now_add=True)
    date_fin = models.DateTimeField(null=True)

    @classmethod
    def getDernierePesee(self):
        return Pesee.objects.last()

    @classmethod
    def estVide(self):
        if len(Pesee.objects.all()) > 0:
            return False
        else:
            return True

    def estTerminee(self):
        if self.date_fin == None:
            return False
        return True


    def finDePesee(self):
        self.date_fin = datetime.datetime.now()
        self.save()

class Poids(models.Model):
    poids = models.IntegerField()
    pesee_id = models.ForeignKey(Pesee, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class Pesage:
    _started: bool = False
    peseeId=None

    @classmethod
    def start(self,pesee):
        self._started = True
        self.peseeId = pesee.id

        #TODO make a class for config the file
        payload = {
            "POIDS_MIN": pesee.poids_min,
            "POIDS_MAX": pesee.poids_max,
            "TARE": pesee.tare
        }
        config_pesee = open("config_pesee.json","w")
        json.dump(payload, config_pesee)

        config_pesee.close()

    @classmethod
    def stop(self):

        self._started = False
        self.peseeId = None

    @classmethod
    def isStarted(self):
        return self._started

    @classmethod
    def restart(self, pesee):
        self._started = True
        self.peseeId = pesee.id
