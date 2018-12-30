import os

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
import logging

from pese_canards import settings
from website.forms import PeseeForm
from website.models import Pesee, Pesage


def index(request):

    return render(request, 'base.html', locals())


def pesee(request):
    return render(request,
                  'pesee.html',
                  {"pesage": Pesage.isStarted()})


def startPesee(request):
    form = PeseeForm(request.POST)


    if form.is_valid():
        form.save()
        pesee = Pesee.getDernierePesee()
        Pesage.start(pesee)

    return redirect("/pesee", pesage=Pesage.isStarted())

def stopPesee(request):

    peseeToStop = Pesee.getDernierePesee()
    peseeToStop.finDePesee()
    Pesage.stop()


    return redirect("/telechargements")


def telechargements(request):
    return render(request, "telechargements.html",{"pesees": Pesee.objects.exclude(date_fin=None)})


def deletePesee(request, pesee_id):

    peseeToDelete = Pesee.objects.get(id=pesee_id)
    print(str(peseeToDelete.fichier.path))
    os.remove(peseeToDelete.fichier.path)
    peseeToDelete.delete()
    return redirect("/telechargements")


def downloadFile(request, pesee_id):
    fichier = Pesee.objects.get(id=pesee_id).fichier

    fichier.open("rb")
    response = HttpResponse(fichier.read(),content_type="application/vnd.ms-excel")
    return response