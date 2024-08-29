from audioop import reverse

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from maquinas.models import Maquina
from .forms import MaquinaForm

def maquinas(request):
    return render(request, "maquinas.html")

def createMaquina(request):

    return render(request, 'createMaquina.html', {"MaquinaForm": MaquinaForm, "exibeMaquina": Maquina.objects.order_by('numeroSerie')})
