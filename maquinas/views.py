
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.template.context_processors import request

from maquinas.models import Maquina
from .forms import MaquinaForm

def maquinas(request):
    return render(request, "maquinas.html")

def createMaquina(request):
    if request.method == 'POST':
        form = MaquinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('createMaq')
    else:
        form = MaquinaForm()

    exibeMaquina = Maquina.objects.order_by('numeroSerie')
    return render(request, 'createMaquina.html', {"MaquinaForm": form, "exibeMaquina": exibeMaquina})


def createUpdate(request, id):
    # Obtém a máquina a ser atualizada
    maquina = get_object_or_404(Maquina, id=id)

    if request.method == "POST":
        # Cria um formulário com os dados enviados pelo usuário
        form = MaquinaForm(request.POST, instance=maquina)

        if form.is_valid():
            # Atualiza a instância de Maquina com os novos dados
            form.save()
            # Redireciona para a mesma view após a atualização
            return redirect(reverse('createMaq'))
    else:
        # Cria um formulário com os dados da máquina existente
        form = MaquinaForm(instance=maquina)

    # Carrega todas as máquinas para exibição
    maquinas = Maquina.objects.order_by('numeroSerie')
    return render(request, 'createMaquina.html', {"form": form, "exibeMaquina": maquinas, "edit_mode": True})



def desativaMaquina(request, id):
    desativa = get_object_or_404(Maquina, id=id)
    if desativa.status == 0:
        desativa.status = 1
        desativa.save()
    elif desativa.status == 1:
        desativa.status = 0
        desativa.save()
    return HttpResponseRedirect(reverse('createMaq'))

def deletaMaquina(request):
    if request.method == "POST":
        id = request.POST.get('id')
        item = get_object_or_404(Maquina, id=id)
        item.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, safe=False)




