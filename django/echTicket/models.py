from django.db import models
from .classesPy.Ticket import Ticket

class Com(models.Model):
    auteur = models.CharField(max_length=255)
    note = models.IntegerField()
    titre = models.CharField(max_length=255)
    contenu = models.TextField()
    date = models.DateField()
    like = models.IntegerField()

    def __str__(self):
        return f"{self.titre} - {self.auteur}"

class Evenement(models.Model):
    nom = models.CharField(max_length=255)
    date = models.DateField()
    lieu = models.CharField(max_length=255)
    # Assumez que Ticket soit un modèle Django déjà défini
    tickets_disponibles = models.ManyToManyField(Ticket, related_name='evenement_tickets')

    def __str__(self):
        return self.nom

class Ticket(models.Model):
    ticket_id = models.CharField(max_length=255)
    event_name = models.CharField(max_length=255)
    price = models.FloatField()
    availability = models.BooleanField(default=True)
    owner = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, related_name='owned_tickets')
    # Ajoutez d'autres champs si nécessaire

    def __str__(self):
        return f"{self.event_name} - {self.ticket_id}"
