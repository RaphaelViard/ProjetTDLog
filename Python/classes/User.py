from typing import Literal
from Ticket import Ticket
from Transac import Transaction

Colors = Literal["RED", "BLUE", "ORANGE", "BROWN", "PURPLE ", "YELLOW", "WHITE", "BLACK"]

class User:
    def __init__(self : str,password : str,username : str,email : str,ticketstosale : list[Ticket],ticketowned : list[Ticket], solde : float, color : Colors):
        self._password = password
        self.username = username
        self.email = email
        self.ticketstosale = ticketstosale #The tickets we are trying to sell
        self.ticketowned = ticketowned #The tickets we own (!= tickets we sell)
        self.solde = solde #Money the user has on his account
        self.color = color

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, newpassword):
        self._password = newpassword

    def acheter_ticket(self, ticket):
        if self.solde >= ticket.prix and ticket.disponibilite:
            self.solde -= ticket.prix
            ticket.availability = False
            ticket.owner = self
            self.ticketowned.append(ticket)
            print(f"{self.username} a acheté le ticket {ticket.id} pour l'événement {ticket.nom}.")
        else:
            print("Achat impossible. Solde insuffisant ou ticket non disponible.")

    def vendre_ticket(self, ticket, acheteur, prix):
        if ticket in self.ticketowned and ticket.owner == self:
            transaction = Transaction(acheteur, self, prix, ticket.nom)
            acheteur.solde -= prix
            self.solde += prix
            ticket.owner = acheteur
            acheteur.ticketowned.append(ticket)
            self.ticketowned.remove(ticket)
            print(f"{self.username} a vendu le ticket {ticket.id} à {acheteur.username} pour {prix}.")
            return transaction
        else:
            print("Vente impossible. Ticket non détenu par l'utilisateur ou transaction invalide.")

    def afficher_ticketowned(self):
        if self.ticketowned:
            print(f"{self.username} possède les tickets suivants:")
        for ticket in self.ticketowned:
            print(f" - {ticket.event_name} ({ticket.price} €)")
        else:
            print(f"{self.username} ne possède aucun ticket.")



