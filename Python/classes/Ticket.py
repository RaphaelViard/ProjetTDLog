class Ticket:
    def __init__(self, ticket_id, event, price, availability=True, owner=None):
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
    def set_price(self, new_price):
        self._price = new_price

    @availability.setter
    def set_availability(self, new_availability):
        self._availability = new_availability

    @owner.setter
    def set_owner(self, new_owner):
        self._owner = new_owner

    ## exchanges

    def purchase(self, buyer):
        if self.availability:
            self._owner = buyer
            self._availability = False
            print(f"Ticket {self.ticket_id} for {self.event} has been purchased by {buyer.username}.")
        else:
            print(f"Ticket {self.ticket_id} for {self.event} is no longer available.")

    ### °°° other functions °°°
