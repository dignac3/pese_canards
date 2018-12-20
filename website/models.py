from django.db import models
from django.utils import timezone

# Create your models here.
class Pesee(models.Model):

    id = models.BigIntegerField(primary_key=True,auto_created=True)
    chemin_acces = models.CharField(max_length=100, default="")


    semaine = models.IntegerField()
    poids_min = models.IntegerField()
    poids_max = models.IntegerField()
    tare = models.IntegerField()

    date_debut = models.DateField(default=timezone.now())
    date_fin = models.DateField(null=True)