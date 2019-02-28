import json

from django.http import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from website.models import Pesage, Pesee
from website.models import Poids


@csrf_exempt
def ajouterPoids(request):
    received_json_data = json.loads(request.body.decode('utf-8'))

    print("Pesage sans id")
    if Pesage.isStarted():
        print("Pesage avec id : " + str(Pesage.peseeId))

        poids_recup= Poids(poids=received_json_data['poids'],pesee_id=Pesee.objects.get(id=Pesage.peseeId))
        poids_recup.save()

    return HttpResponse()
