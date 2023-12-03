from typing import Literal,List

Colors = Literal["RED", "BLUE", "ORANGE", "BROWN", "PURPLE", "YELLOW", "WHITE", "BLACK"]

class User:
    def __init__(self, password:str, username:str, email:str, tickets_to_sale,
                 tickets_owned, solde:float, color: Colors, comments, image: str, bio: str,
                 event_interested, purchase_history, followers,
                 following: List[str]):
        self._password: str = password
        self._username: str = username
        self._email: str = email
        self._solde: float = solde
        self._color: Colors = color
        self._image: str = image
        self._bio: str = bio
        self._tickets_to_sale = []
        self._comments = []
        self._followers = []
        self._following = []
        self._tickets_owned = []  #
        self._event_interested = []  #
        self._purchase_history = []  #

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

        def add_ticket_to_sale(self, new_ticket):
            self._tickets_to_sale.append(new_ticket)

        def remove_ticket_to_sale(self, ticket_to_remove):
            if ticket_to_remove in self._tickets_to_sale:
                self._tickets_to_sale.remove(ticket_to_remove)

        def add_ticket_owned(self, new_ticket):
            self._tickets_owned.append(new_ticket)

        def remove_ticket_owned(self, ticket_to_remove):
            if ticket_to_remove in self._tickets_owned:
                self._tickets_owned.remove(ticket_to_remove)

        def add_comment(self, new_comment):
            self._comments.append(new_comment)

        def remove_comment(self, comment_to_remove):
            if comment_to_remove in self._comments:
                self._comments.remove(comment_to_remove)

        def add_event_interested(self, new_event):
            self._event_interested.append(new_event)

        def remove_event_interested(self, event_to_remove):
            if event_to_remove in self._event_interested:
                self._event_interested.remove(event_to_remove)

        def add_purchase_history(self, new_transaction):
            self._purchase_history.append(new_transaction)

        def remove_purchase_history(self, transaction_to_remove):
            if transaction_to_remove in self._purchase_history:
                self._purchase_history.remove(transaction_to_remove)

        def add_follower(self, new_follower):
            self._followers.append(new_follower)

        def remove_follower(self, follower_to_remove):
            if follower_to_remove in self._followers:
                self._followers.remove(follower_to_remove)

        def add_following(self, new_following):
            self._following.append(new_following)

        def remove_following(self, following_to_remove):
            if following_to_remove in self._following:
                self._following.remove(following_to_remove)

        ## functions

        def sell_ticket(self, ticket, buyer, price):
            from Transac import Transaction
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

        def add_follower(self, new_follower: str):
            """
            Add a follower to the user's profile.
            """
            self._followers.append(new_follower)

        def remove_follower(self, follower_to_remove: str):
            """
            Remove a follower from the user's profile.
            """
            if follower_to_remove in self._followers:
                self._followers.remove(follower_to_remove)

        def add_following(self, new_following: str):
            """
            Add a user to the list of people followed by the user.
            """
            self._following.append(new_following)

        def remove_following(self, following_to_remove: str):
            """
            Remove a user from the list of people followed by the user.
            """
            if following_to_remove in self._following:
                self._following.remove(following_to_remove)

        def display_followers(self):
            """
            Display the list of followers for the user.
            """
            if self._followers:
                print(f"{self._username} has the following followers:")
                for follower in self._followers:
                    print(f" - {follower}")
            else:
                print(f"{self._username} has no followers.")

        def display_following(self):
            """
            Display the list of people followed by the user.
            """
            if self._following:
                print(f"{self._username} follows the following people:")
                for user in self._following:
                    print(f" - {user}")
            else:
                print(f"{self._username} is not following anyone.")

        def update_bio(self, new_bio: str):
            """
            Update the user's biography.
            """
            self._bio = new_bio
            print(f"The biography of {self._username} has been updated.")

        def update_image(self, new_image: str):
            """
            Update the user's profile image.
            """
            self._image = new_image
            print(f"The profile image of {self._username} has been updated.")

        def add_comment_to_event(self, event, new_comment):
            """
            Add a comment to a specific event.
            """
            if event in self._event_interested:
                event.add_comment(new_comment)
                print(f"{self._username} added a comment to the event: {event.name}")
            else:
                print(f"{self._username} cannot add a comment to an event they are not interested in.")

        def display_comments_on_events(self):
            """
            Display the comments made by the user on various events.
            """
            if self._comments:
                print(f"{self._username}'s comments on events:")
                for comment in self._comments:
                    print(f" - {comment.event_name}: {comment.text}")
            else:
                print(f"{self._username} has not made any comments on events.")

class IndividualUser(User):
    def __init__(self, password: str, username: str, email: str, tickets_to_sale,
                 tickets_owned, solde: float, color: Colors, comments, image: str, bio: str,
                 event_interested, purchase_history, followers,
                 following: List[str], date_of_birth, address):
        super().__init__(password, username, email, tickets_to_sale, tickets_owned, solde, color,
                         comments, image, bio, event_interested, purchase_history, followers, following)
        self._date_of_birth: str = date_of_birth
        self._address: str = address

    # Additional property and setter for IndividualUser

    @property
    def date_of_birth(self) -> str:
        return self._date_of_birth

    @property
    def address(self) -> str:
        return self._address

    @date_of_birth.setter
    def date_of_birth(self, new_date_of_birth: str):
        self._date_of_birth = new_date_of_birth

    @address.setter
    def address(self, new_address: str):
        self._address = new_address

    def display_purchase_history(self):  #
        """
        Display the user's purchase history.
        """
        if self._purchase_history:
            print(f"{self._username} has the following purchase history:")
            for transaction in self._purchase_history:
                print(f" - {transaction}")
        else:
            print(f"{self._username} has no purchase history.")

    def buy_ticket(self, ticket):
        if self._solde >= ticket.price and ticket.availability:
            self._solde -= ticket.price
            ticket.availability = False
            ticket.owner = self
            self._tickets_owned.append(ticket)
            print(f"{self._username} has bought ticket {ticket.id} for the event {ticket.event_name}.")
        else:
            print("Purchase impossible. Insufficient balance or ticket not available.")

    def display_tickets_owned(self):
        if self._tickets_owned:
            print(f"{self._username} owns the following tickets:")
        for ticket in self._tickets_owned:
            print(f" - {ticket.event_name} ({ticket.price} €)")
        else:
            print(f"{self._username} owns no tickets.")

    def add_event_interest(self, new_event):
        """
        Add an event to the user's list of interests.
        """
        self._event_interested.append(new_event)
        print(f"{self._username} is now interested in the event: {new_event.name}")

    def remove_event_interest(self, event_to_remove):
        """
        Remove an event from the user's list of interests.
        """
        if event_to_remove in self._event_interested:
            self._event_interested.remove(event_to_remove)
            print(f"{self._username} is no longer interested in the event: {event_to_remove.name}")

    def display_event_interests(self):  #
        """
        Display the events that the user is interested in.
        """
        if self._event_interested:
            print(f"{self._username} is interested in the following events:")
            for event in self._event_interested:
                print(f" - {event.name}")
        else:
            print(f"{self._username} has no specific event interests.")

class OrganizationUser(User):
    def __init__(self, password: str, username: str, email: str, tickets_to_sale,
                 solde: float, color: Colors, comments, image: str, bio: str,
                 followers: List[str], following: List[str], organization_name: str, registration_number: str):
        super().__init__(username, password , email, tickets_to_sale, [], color, solde,
                         comments, image, bio, [], [], followers, following)
        self._organization_name: str = organization_name
        self._registration_number: str = registration_number

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

    ### °°° other functions °°°