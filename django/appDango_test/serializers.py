# serializers.py

from rest_framework import serializers
from .models import ProfilUtilisateur, Evenement, Ticket, Achat, Commentaire

class ProfilUtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilUtilisateur
        fields = '__all__'

class EvenementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evenement
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class AchatSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True, read_only=True)

    class Meta:
        model = Achat
        fields = '__all__'

class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaire
        fields = '__all__'
