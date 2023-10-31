from django.shortcuts import render
from django.http import HttpResponse

def template_view(request):
    # Logique de traitement ici
    return render(request, 'templates/base.html')
