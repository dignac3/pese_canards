import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from backend.forms import PoidsForm
from backend.models import Poids


@csrf_exempt
def ajouterPoids(request):
    received_json_data = json.loads(request.body)

    poidsRecu= Poids(poids=received_json_data['poids'])

    poidsRecu.save()

    return HttpResponse()
