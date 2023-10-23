from django.shortcuts import render
from django.http import HttpResponse

def ma_vue(request):
    # Votre logique de traitement ici
    contenu = "Bienvenue dans ma première vue Django !"
    return HttpResponse(contenu)
