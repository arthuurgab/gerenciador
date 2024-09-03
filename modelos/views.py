from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import ModelosForm, UpdateModeloForm
from .models import Modelos
from django.http import HttpResponseRedirect, JsonResponse


def modelos(request):
    if request.method == 'POST':
        form = ModelosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('modelos')
    else:
        form = ModelosForm()

    exibeModelo = Modelos.objects.order_by('id')
    return render(request, "modelos.html", {"ModeloForm": form, "exibeModelo": exibeModelo})

def updateModelo(request, id):
    modelo = get_object_or_404(Modelos, id=id)
    if request.method == "POST":
        form = UpdateModeloForm(request.POST, instance=modelo)

        if form.is_valid():
            form.save()
            return redirect(reverse('modelos'))
    else:
        form = UpdateModeloForm(instance=modelo)

    modelos = Modelos.objects.order_by('id')
    return JsonResponse()

def deletaModelo(request):
    if request.method == "POST":
        id = request.POST.get('id')
        item = get_object_or_404(Modelos, id=id)
        item.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, safe=False)