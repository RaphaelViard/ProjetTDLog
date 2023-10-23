from django.shortcuts import render
from django.http import HttpResponse

def ma_vue(request):
    # Votre logique de traitement ici
    contenu = "Ouais le gabzz"
    return HttpResponse(contenu)
