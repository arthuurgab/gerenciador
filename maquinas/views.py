from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from maquinas.models import Maquina
from .forms import MaquinaForm

def maquinas(request):
    return render(request, "maquinas.html")


def createMaquina(request):
    if request.method == 'POST':
        form = MaquinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('maquina')
    else:
        form = MaquinaForm()

    context = {'form': form}
    return render(request, 'createMaquina.html', context)