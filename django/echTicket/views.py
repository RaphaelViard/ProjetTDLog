from rest_framework import generics
from .models import Com, Evenement, Ticket
from .serializers import ComSerializer, EvenementSerializer, TicketSerializer

class ComListCreateView(generics.ListCreateAPIView):
    queryset = Com.objects.all()
    serializer_class = ComSerializer

class EvenementListCreateView(generics.ListCreateAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer

class TicketListCreateView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer