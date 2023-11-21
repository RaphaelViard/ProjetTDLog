# views.py

from rest_framework import generics
from .models import ProfilUtilisateur, Evenement, Ticket, Achat, Commentaire
from .serializers import ProfilUtilisateurSerializer, EvenementSerializer, TicketSerializer, AchatSerializer, CommentaireSerializer

class ProfilUtilisateurListe(generics.ListCreateAPIView):
    queryset = ProfilUtilisateur.objects.all()
    serializer_class = ProfilUtilisateurSerializer

class ProfilUtilisateurDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProfilUtilisateur.objects.all()
    serializer_class = ProfilUtilisateurSerializer

class EvenementListe(generics.ListCreateAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer

class EvenementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer

class TicketListe(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class AchatListe(generics.ListCreateAPIView):
    queryset = Achat.objects.all()
    serializer_class = AchatSerializer

class AchatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Achat.objects.all()
    serializer_class = AchatSerializer

class CommentaireListe(generics.ListCreateAPIView):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer

class CommentaireDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer
