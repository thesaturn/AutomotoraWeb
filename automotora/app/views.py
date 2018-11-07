from django.shortcuts import render, HttpResponse
from .forms import VehiculoForm
from .models import Vehiculo
# Create your views here.

def home(request):
    return render(request, 'registro.html')

def registro(request):
    return render(request, 'registroauto.html')

def auto_vista_test(request):
    form = VehiculoForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'registrotest.html', context)
