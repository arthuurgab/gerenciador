from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, reverse
from maquinas.models import Maquina
from .forms import MaquinaForm
from .forms import MaquinaUpdate

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




