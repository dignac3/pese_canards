
from django.shortcuts import render

# Create your views here.
import logging

def index(request):

    return render(request, 'base.html', locals())

