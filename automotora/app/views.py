from django.shortcuts import render, HttpResponse

from .forms import AutoForm

from .models import Auto
# Create your views here.

def home(request):
    return render(request, 'registro.html')

def registro(request):
    return render(request, 'registroauto.html')

def auto_vista_test(request):
    form = AutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AutoForm()

    context = {
        'form': form
    }
    return render(request, 'registrotest.html', context)
