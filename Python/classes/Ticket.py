class Ticket:
    def __init__(self, ticket_id, event_name, price, availability=True, owner=None):
        self.ticket_id = ticket_id
        self.event_name = event_name
        self.price = price
        self.availability = availability
        self.owner = owner
        self.comments = []

    def purchase(self, buyer):
        if self.availability:
            self.owner = buyer
            self.availability = False
            print(f"Le ticket {self.ticket_id} pour {self.event_name} a été acheté par {buyer.username}.")
        else:
            print(f"Le ticket {self.ticket_id} pour {self.event_name} n'est plus disponible.")

    def exchange(self, new_owner):
        if self.owner:
            self.owner = new_owner
            print(f"Le ticket {self.ticket_id} pour {self.event_name} a été échangé à {new_owner.username}.")
        else:
            print(f"Le ticket {self.ticket_id} pour {self.event_name} n'a pas encore été acheté.")

    def add_comment(self, comment):
        self.comments.append(comment)
        print("Commentaire ajouté avec succès.")
