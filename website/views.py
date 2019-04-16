import csv
import os

from django.http import HttpResponse
from django.shortcuts import render, redirect

from website.forms import PeseeForm
from website.models import Pesee, Pesage, Poids


def index(request):

    return render(request, 'base.html', locals())


def pesee(request):

    if not Pesee.estVide():
        #TODO Faire une page dédiée
        #S'il existe des pesées
        lastPesee = Pesee.getDernierePesee()
        if not Pesage.isStarted() and not lastPesee.estTerminee() :
            # S'il n'y a pas de Pesée en cours mais que la dernière pesée ne s'est pas terminé

            #Actuellement on relance sur la dernière Pesée et la page de gestion va la supprimer si besoin
            #Pesage.start(lastPesee)

            #On va renvoyer vers la page de gestions
            return render(
                request,
                'restarting.html',
                {
                    "pesee_id": lastPesee.id
                }
            )

    return render(request,
                  'pesee.html',
                  {"pesage_started": Pesage.isStarted(),
                   "pesee_id":Pesage.peseeId})


def startPesee(request):
    form = PeseeForm(request.POST)


    if form.is_valid():
        form.save()

        pesee = Pesee.getDernierePesee()
        Pesage.start(pesee)

        return redirect("/pesee", pesage=Pesage.isStarted(), pesee_id=Pesage.peseeId)

def restartPesee(request):
    pesee = Pesee.getDernierePesee()
    Pesage.restart(pesee)

    return redirect("/pesee", pesage=Pesage.isStarted(), pesee_id=Pesage.peseeId)

def cancelPesee(request):
    peseeToStop = Pesee.getDernierePesee()
    peseeToStop.finDePesee()
    Pesage.stop()
    return redirect("/telechargements")
def stopPesee(request):

    peseeToStop = Pesee.objects.get(id=Pesage.peseeId)
    peseeToStop.finDePesee()
    Pesage.stop()
    return redirect("/telechargements")


def telechargements(request):
    return render(request, "telechargements.html",{"pesees": Pesee.objects.exclude(date_fin=None)})

def deletePesee(request, pesee_id):

    Pesee.objects.get(id=pesee_id).delete()

    return redirect("/telechargements")


def downloadFile(request,pesee_id):
    pesee = Pesee.objects.get(id = pesee_id)
    liste_poids = Poids.objects.filter(pesee_id=pesee_id)
    filename = "pesee" + str(pesee.id )+ "_sem" + str(pesee.semaine) + "_" + pesee.date_debut.strftime('%d-%m-%Y')

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="'+filename+'.csv"'

    writer = csv.writer(response)
    writer.writerow(['Poids', 'Date'])

    print(str(liste_poids.count()))
    if liste_poids.count() > 0:
        for poids in liste_poids:
            writer.writerow([poids.poids, poids.date.strftime("%d/%m/%Y %H:%M:%S")])



    return response