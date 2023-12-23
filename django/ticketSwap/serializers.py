from rest_framework import serializers
from .models import Com, Evenement, Ticket

class ComSerializer(serializers.ModelSerializer):
    class Meta:
        model = Com
        fields = '__all__'

class EvenementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evenement
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'