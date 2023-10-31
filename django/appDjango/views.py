from django.shortcuts import render
from django.http import HttpResponse

def test_view(request):
    # Votre logique de traitement ici
    content = "Ouais le gabzz"
    return HttpResponse(content)

def template_view(request):
    # Logique de traitement ici
    return render(request, 'templates/base.html')
