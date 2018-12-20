from django.db import models
from django.utils import timezone

# Create your models here.


class Poids(models.Model):
    poids = models.IntegerField()
    date = models.DateField(default=timezone.now())