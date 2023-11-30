from Event import Event
from User import User

class Ticket:
    def __init__(self, ticket_id, event: Event, price: float, availability=True, owner: User = None):
        self._ticket_id = ticket_id
        self._event = event
        self._price = price
        self._availability = availability
        self._owner = owner

    ## property / setter

    @property
    def ticket_id(self):
        return self._ticket_id

    @property
    def event(self):
        return self._event

    @property
    def price(self):
        return self._price

    @property
    def availability(self):
        return self._availability

    @property
    def owner(self):
        return self._owner

    @price.setter
    def price(self, new_price):
        self._price = new_price

    @availability.setter
    def availability(self, new_availability):
        self._availability = new_availability

    @owner.setter
    def owner(self, new_owner):
        self._owner = new_owner

    ## display

    def display_ticket_info(self):
        print(f"Ticket ID: {self.ticket_id}")
        print(f"Event Name: {self.event.name}")
        print(f"Price: {self.price} €")
        print(f"Availability: {'Available' if self.availability else 'Sold'}")
        print(f"Owner: {self.owner.username if self.owner else 'None'}")

    ## update

    def upgrade_ticket(self, new_event: Event, new_price: float):
        if self.availability:
            self._event = new_event
            self._price = new_price
            print(f"Ticket {self.ticket_id} has been upgraded to {new_event.name} with a new price of {new_price} €.")
        else:
            print(f"Upgrade is not applicable for sold or reserved Ticket {self.ticket_id}.")

    ## transfer operations

    def purchase(self, buyer: User):
        if self.availability:
            if buyer.solde >= self.price:
                self._owner = buyer
                self._availability = False
                buyer.solde -= self.price  # Deduct the price from the buyer's balance
                print(f"Ticket {self.ticket_id} for {self.event.name} has been purchased by {buyer.username}.")
            else:
                print("Insufficient funds to purchase the ticket.")
        else:
            print(f"Ticket {self.ticket_id} for {self.event.name} is no longer available.")

    def transfer_ownership(self, new_owner: User):
        if self.availability and self.owner:
            self.owner.remove_ticket_owned(self)
            self.owner = new_owner
            new_owner.add_ticket_owned(self)
            print(f"Ticket {self.ticket_id} has been transferred to {new_owner.username}.")
        else:
            print("Ticket is not available for transfer.")

    def refund(self):
        if not self.availability and self.owner:
            self.owner.solde += self.price
            self.owner = None
            self.availability = True
            print(f"Ticket {self.ticket_id} has been refunded.")
        else:
            print("Refund is not applicable for this ticket.")

    def reserve_ticket(self, user: User):
        if self.availability:
            self.availability = False
            self.owner = user
            print(f"Ticket {self.ticket_id} has been reserved by {user.username}.")
        else:
            print(f"Ticket {self.ticket_id} is not available for reservation.")

    def cancel_reservation(self):
        if not self.availability and self.owner:
            self.availability = True
            reserved_user = self.owner
            self.owner = None
            print(f"Reservation for Ticket {self.ticket_id} has been canceled by {reserved_user.username}.")
        else:
            print(f"No reservation to cancel for Ticket {self.ticket_id}.")

    ## get

    def get_ticket_details(self):
        details = {
            "Ticket ID": self.ticket_id,
            "Event Name": self.event.name,
            "Price": self.price,
            "Availability": self.availability,
            "Owner": self.owner.username if self.owner else "None"
        }
        return details

    def get_ticket_status(self):
        if self.availability:
            return "Available"
        elif self.owner:
            return f"Sold to {self.owner.username}"
        else:
            return "Refunded"

    ## verification

    def is_owned_by(self, user: User):
        return self.owner == user

    def is_available(self):
        return self.availability

    def update_ticket_info(self, new_event: Event, new_price: float):
        self._event = new_event
        self._price = new_price
        print(f"Ticket {self.ticket_id} information updated.")

    def check_ticket_validity(self):
        if not self.availability and self.owner:
            print(f"Ticket {self.ticket_id} is valid.")
            return True
        else:
            print(f"Ticket {self.ticket_id} is not valid.")
            return False

    ### °°° other functions °°°

    # idée -> appliquer des réductions ?
    # idée -> ajouter QR code