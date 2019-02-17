import json

from django.http import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from website.models import Pesage
from website.models import Poids


@csrf_exempt
def ajouterPoids(request):
    received_json_data = json.loads(request.body)


    if Pesage.isStarted():
        poids_recup= Poids(poids=received_json_data['poids'],pesee_id=Pesage.peseeId)
        poids_recup.save()

    return HttpResponse()
