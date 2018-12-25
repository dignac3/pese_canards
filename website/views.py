
from django.shortcuts import render

# Create your views here.
import logging

def index(request):

    return render(request, 'base.html', locals())


def pesee(request):
    return render(request,'pesee.html',locals())
