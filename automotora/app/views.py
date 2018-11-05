from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'registro.html')

def registro(request):
    return render(request, 'registroauto.html')
