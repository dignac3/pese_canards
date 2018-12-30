import csv
import datetime
import json
import os

from django.core.files import File
from django.db import models
from django.utils import timezone

# Create your models here.
from backend.models import Poids

EXTENSION = ".csv"

FILES_PATH = "files/"




class Pesee(models.Model):

    fichier = models.FileField(upload_to=(FILES_PATH))


    semaine = models.IntegerField()
    poids_min = models.IntegerField()
    poids_max = models.IntegerField()
    tare = models.IntegerField()

    date_debut = models.DateTimeField(auto_now_add=True)
    date_fin = models.DateTimeField(null=True)

    @classmethod
    def getDernierePesee(self):
        return Pesee.objects.last()

    def ecrirePoidsDansFichierEtSupprimer(self):

        path = os.path.join(FILES_PATH, self.genererNomFichier())
        fic = open(path,"w+")

        writer = csv.writer(fic,"excel")

        nom_colonnes = ["Date","Poids"]
        writer.writerow(nom_colonnes)

        for poids in Poids.objects.all().filter(date__gt=self.date_debut).filter(date__lt=self.date_fin):
            writer.writerow([poids.date,poids.poids])

        Poids.objects.all().delete()
        self.fichier.save(self.genererNomFichier(), File(fic))
        os.remove(path)

        fic.close()



    def finDePesee(self):
        self.date_fin = datetime.datetime.now()
        self.save()

        self.ecrirePoidsDansFichierEtSupprimer()

        return self

    def genererNomFichier(self):
        return "Pesee_" + str(self.id) + "_sem_"+ str(self.semaine) + "_date_" + str(self.date_debut.date()) + ".csv"


class Pesage:
    _started = False


    @classmethod
    def start(self,pesee):
        self._started = True

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



    @classmethod
    def isStarted(self):
        return self._started


