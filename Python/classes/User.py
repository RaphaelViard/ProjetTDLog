from typing import List, Literal
from Ticket import Ticket
from Transac import Transaction
from Event import Event
from Com import Comment

Colors = Literal["RED", "BLUE", "ORANGE", "BROWN", "PURPLE", "YELLOW", "WHITE", "BLACK"]

class User:
    def __init__(self, password: str, username: str, email: str, tickets_to_sale: List[Ticket],
                 tickets_owned: List[Ticket], solde: float, color: Colors, comments: List[Comment], image: str, bio: str,
                 event_interested: List[Event], purchase_history: List[Transaction], followers: List[str],
                 following: List[str]):
        self._password = password
        self._username = username
        self._email = email
        self._solde = solde
        self._color = color
        self._image = image
        self._bio = bio
        self._tickets_to_sale = tickets_to_sale
        self._tickets_owned = tickets_owned
        self._comments = comments
        self._event_interested = event_interested
        self._purchase_history = purchase_history
        self._followers = followers
        self._following = following

        @property
        def password(self):
            return self._password

        @property
        def username(self):
            return self._username

        @property
        def email(self):
            return self._email

        @property
        def tickets_to_sale(self):
            return self._tickets_to_sale

        @property
        def tickets_owned(self):
            return self._tickets_owned

        @property
        def solde(self):
            return self._solde

        @property
        def color(self):
            return self._color

        @property
        def comments(self):
            return self._comments

        @property
        def image(self):
            return self._image

        @property
        def bio(self):
            return self._bio

        @property
        def event_interested(self):
            return self._event_interested

        @property
        def purchase_history(self):
            return self._purchase_history

        @property
        def followers(self):
            return self._followers

        @property
        def following(self):
            return self._following

        # Setters

        @password.setter
        def password(self, new_password):
            self._password = new_password

        @username.setter
        def username(self, new_username):
            self._username = new_username

        @email.setter
        def email(self, new_email):
            self._email = new_email

        @tickets_to_sale.setter
        def tickets_to_sale(self, new_tickets_to_sale):
            self._tickets_to_sale = new_tickets_to_sale

        @tickets_owned.setter
        def tickets_owned(self, new_tickets_owned):
            self._tickets_owned = new_tickets_owned

        @solde.setter
        def solde(self, new_solde):
            self._solde = new_solde

        @color.setter
        def color(self, new_color):
            self._color = new_color

        @comments.setter
        def comments(self, new_comments):
            self._comments = new_comments

        @image.setter
        def image(self, new_image):
            self._image = new_image

        @bio.setter
        def bio(self, new_bio):
            self._bio = new_bio

        @event_interested.setter
        def event_interested(self, new_event_interested):
            self._event_interested = new_event_interested

        @purchase_history.setter
        def purchase_history(self, new_purchase_history):
            self._purchase_history = new_purchase_history

        @followers.setter
        def followers(self, new_followers):
            self._followers = new_followers

        @following.setter
        def following(self, new_following):
            self._following = new_following

        def add_ticket_to_sale(self, new_ticket: Ticket):
            self._tickets_to_sale.append(new_ticket)

        def remove_ticket_to_sale(self, ticket_to_remove: Ticket):
            if ticket_to_remove in self._tickets_to_sale:
                self._tickets_to_sale.remove(ticket_to_remove)

        def add_ticket_owned(self, new_ticket: Ticket):
            self._tickets_owned.append(new_ticket)

        def remove_ticket_owned(self, ticket_to_remove: Ticket):
            if ticket_to_remove in self._tickets_owned:
                self._tickets_owned.remove(ticket_to_remove)

        def add_comment(self, new_comment: Comment):
            self._comments.append(new_comment)

        def remove_comment(self, comment_to_remove: Comment):
            if comment_to_remove in self._comments:
                self._comments.remove(comment_to_remove)

        def add_event_interested(self, new_event: Event):
            self._event_interested.append(new_event)

        def remove_event_interested(self, event_to_remove: Event):
            if event_to_remove in self._event_interested:
                self._event_interested.remove(event_to_remove)

        def add_purchase_history(self, new_transaction: Transaction):
            self._purchase_history.append(new_transaction)

        def remove_purchase_history(self, transaction_to_remove: Transaction):
            if transaction_to_remove in self._purchase_history:
                self._purchase_history.remove(transaction_to_remove)

        def add_follower(self, new_follower: str):
            self._followers.append(new_follower)

        def remove_follower(self, follower_to_remove: str):
            if follower_to_remove in self._followers:
                self._followers.remove(follower_to_remove)

        def add_following(self, new_following: str):
            self._following.append(new_following)

        def remove_following(self, following_to_remove: str):
            if following_to_remove in self._following:
                self._following.remove(following_to_remove)

class IndividualUser(User):
    def __init__(self, password: str, username: str, email: str, tickets_to_sale: List[Ticket],
                 tickets_owned: List[Ticket], solde: float, color: Colors, comments: List[Comment], image: str, bio: str,
                 event_interested: List[Event], purchase_history: List[Transaction], followers: List[str],
                 following: List[str], date_of_birth: str, address: str):
        super().__init__(password, username, email, tickets_to_sale, tickets_owned, solde, color,
                         comments, image, bio, event_interested, purchase_history, followers, following)
        self._date_of_birth = date_of_birth
        self._address = address

    # Additional property and setter for IndividualUser

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @property
    def address(self):
        return self._address

    @date_of_birth.setter
    def date_of_birth(self, new_date_of_birth):
        self._date_of_birth = new_date_of_birth

    @address.setter
    def address(self, new_address):
        self._address = new_address

class OrganizationUser(User):
    def __init__(self, password: str, username: str, email: str, tickets_to_sale: List[Ticket],
                 solde: float, color: Colors, comments: List[Comment], image: str, bio: str,
                 followers: List[str], following: List[str], organization_name: str, registration_number: str):
        super().__init__(password, username, email, tickets_to_sale, [], solde, color,
                         comments, image, bio, [], [], followers, following)
        self._organization_name = organization_name
        self._registration_number = registration_number

    # Additional property and setter for OrganizationUser

    @property
    def organization_name(self):
        return self._organization_name

    @property
    def registration_number(self):
        return self._registration_number

    @organization_name.setter
    def organization_name(self, new_organization_name):
        self._organization_name = new_organization_name

    @registration_number.setter
    def registration_number(self, new_registration_number):
        self._registration_number = new_registration_number

    ## Functions

    def buy_ticket(self, ticket):
        if self.solde >= ticket.price and ticket.availability:
            self.solde -= ticket.price
            ticket.availability = False
            ticket.owner = self
            self.tickets_owned.append(ticket)
            print(f"{self.username} has bought ticket {ticket.id} for the event {ticket.event_name}.")
        else:
            print("Purchase impossible. Insufficient balance or ticket not available.")

    def sell_ticket(self, ticket, buyer, price):
        if ticket in self.tickets_owned and ticket.owner == self:
            transaction = Transaction(buyer, self, price, ticket.event_name)  # No check for sufficient balance
            buyer.solde -= price
            self.solde += price
            ticket.owner = buyer
            buyer.tickets_owned.append(ticket)
            self.tickets_to_sale.remove(ticket)
            print(f"{self.username} sold ticket {ticket.id} to {buyer.username} for {price}.")
            return transaction
        else:
            print("Sale impossible. User does not own the ticket or invalid transaction.")

    def display_tickets_owned(self):
        if self.tickets_owned:
            print(f"{self.username} owns the following tickets:")
        for ticket in self.tickets_owned:
            print(f" - {ticket.event_name} ({ticket.price} €)")
        else:
            print(f"{self.username} owns no tickets.")

    ### °°° other functions °°°




