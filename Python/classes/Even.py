from Ticket import Ticket

class Evenement:
    def __init__(self, nom, date, lieu):
        self.nom = nom
        self.date = date
        self.lieu = lieu
        self.tickets_disponibles = []

    def creer_ticket(self, ticket_id, prix):
        nouveau_ticket = Ticket(ticket_id, self.nom, prix)
        self.tickets_disponibles.append(nouveau_ticket)
        return nouveau_ticket
    
    #Aller chercher tous les tickets a vendre sur le site pour un seul évnènement (liste de l'ensemble des tickets a vendre pour chaque event ?)