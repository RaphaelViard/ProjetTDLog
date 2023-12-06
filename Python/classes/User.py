from Transac import Transaction
class User:
    def __init__(self, username, password, email=None,
                  color = "BLACK", image=None, solde=0,  bio=None, tickets_to_sale=[],
                  transaction_history=[], comments=[], followers=[],
                  following=[]):
        self._password = password
        self._username= username
        self._email= email
        self._solde= solde
        self._color = color
        self._image = image
        self._bio = bio
        self._tickets_to_sale = tickets_to_sale
        self._comments = comments
        self._followers = followers
        self._following = following
        self._transaction_history = transaction_history

    @property
    def password(self) :
        return self._password

<<<<<<< HEAD
    @property
    def username(self) :
        return self._username

    @property
    def email(self) :
        return self._email

    @property
    def tickets_to_sale(self) :
        return self._tickets_to_sale

    @property
    def solde(self) :
        return self._solde

    @property
    def color(self) :
        return self._color

    @property
    def comments(self) :
        return self._comments

    @property
    def image(self) :
        return self._image

    @property
    def bio(self) :
        return self._bio

    @property
    def event_interested(self) :
        return self._event_interested

    @property
    def transaction_history(self) :
        return self._transaction_history

    @property
    def followers(self) :
        return self._followers

    @property
    def following(self) :
=======
class User:
    def __init__(self, password: str, username: str, email: str, tickets_to_sale: List[Ticket],
                solde: float, color: Colors, comments: List[Comment], image: str, bio: str, transaction_history: List[Transaction], followers: List[str],
                following: List[str]):
        self._password: str = password
        self._username: str = username
        self._email: str = email
        self._solde: float = solde
        self._color: Colors = color
        self._image: str = image
        self._bio: str = bio
        self._tickets_to_sale: List[Ticket] = tickets_to_sale
        self._comments: List[Comment] = comments
        self._followers: List[str] = followers
        self._following: List[str] = following
        self._transaction_history: List[Transaction] = transaction_history

    @property
    def password(self) -> str:
        return self._password

    @property
    def username(self) -> str:
        return self._username

    @property
    def email(self) -> str:
        return self._email

    @property
    def tickets_to_sale(self) -> List[Ticket]:
        return self._tickets_to_sale


    @property
    def solde(self) -> float:
        return self._solde

    @property
    def color(self) -> Colors:
        return self._color

    @property
    def comments(self) -> List[Comment]:
        return self._comments

    @property
    def image(self) -> str:
        return self._image

    @property
    def bio(self) -> str:
        return self._bio

    @property
    def event_interested(self) -> List[Event]:
        return self._event_interested

    @property
    def purchase_history(self) -> List[Transaction]:
        return self._purchase_history

    @property
    def followers(self) -> List[str]:
        return self._followers

    @property
    def following(self) -> List[str]:
>>>>>>> faff86e85f2b86df828a8276360025f458c5acf3
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

<<<<<<< HEAD
    @transaction_history.setter
    def transaction_history(self, new_transaction_history):
        self._transaction_history = new_transaction_history
=======
    @purchase_history.setter
    def purchase_history(self, new_purchase_history):
        self._purchase_history = new_purchase_history
>>>>>>> faff86e85f2b86df828a8276360025f458c5acf3

    @followers.setter
    def followers(self, new_followers):
        self._followers = new_followers

    @following.setter
    def following(self, new_following):
        self._following = new_following
<<<<<<< HEAD

    def add_ticket_to_sale(self, new_ticket):
        self._tickets_to_sale.append(new_ticket)

    def remove_ticket_to_sale(self, ticket_to_remove):
        if ticket_to_remove in self.tickets_to_sale:
            self.tickets_to_sale.remove(ticket_to_remove)

    def add_comment(self, new_comment):
        self.comments.append(new_comment)

    def remove_comment(self, comment_to_remove):
        if comment_to_remove in self.comments:
            self.comments.remove(comment_to_remove)

    def add_transaction_history(self, new_transaction):
        self._transaction_history.append(new_transaction)

    def remove_transaction_history(self, transaction_to_remove):
        if transaction_to_remove in self._purchase_history:
            self._transaction_history.remove(transaction_to_remove)

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

    def sell_ticket(self, ticket, buyer):
        if (buyer.solde < ticket.price):
            print("Solde Insuffisant")
        elif ticket in self.tickets_to_sale and ticket.owner == self:
            transaction = Transaction(self, buyer, ticket.price, ticket)  # No check for sufficient balance
            buyer.solde -= ticket.price
            self.solde += ticket.price
            ticket.owner = buyer
            buyer.tickets_owned.append(ticket)
            self.tickets_to_sale.remove(ticket)
            ticket.availability = False
            print(f"{self.username} sold ticket {ticket.id} to {buyer.username} for {ticket.price}$.")
            return transaction
        else:
            print("Sale impossible. User does not own the ticket or invalid transaction.")

    def display_followers(self):
        if self.followers:
            print(f"{self._username} has the following followers:")
            for follower in self.followers:
                print(f" - {follower}")
        else:
            print(f"{self.username} has no followers.")

    def display_following(self):
        if self._following:
            print(f"{self.username} follows the following people:")
            for user in self._following:
                print(f" - {user}")
        else:
            print(f"{self.username} is not following anyone.")

    def update_bio(self, new_bio: str):
        self._bio = new_bio
        print(f"The biography of {self.username} has been updated.")

    def update_image(self, new_image: str):
        self._image = new_image
        print(f"The profile image of {self.username} has been updated.")

    def add_comment_to_event(self, event, new_comment):
        if event in self._event_interested:
            event.add_comment(new_comment)
            print(f"{self.username} added a comment to the event: {event.name}")
        else:
            print(f"{self.username} cannot add a comment to an event they are not interested in.")

    def display_comments_on_events(self):
        if self.comments:
            print(f"{self.username}'s comments on events:")
            for comment in self.comments:
                print(f" - {comment.event_name}: {comment.text}")
        else:
            print(f"{self.username} has not made any comments on events.")


class IndividualUser(User):
    def __init__(self, username, password, email=None,
                  color = "BLACK", image=None, solde=0,  bio=None, tickets_to_sale=[],
                  transaction_history=[], comments=[], followers=[],
                 following=[], tickets_owned=[], event_interested = []):
        super().__init__(username, password, email,
                  color, image, solde,  bio, tickets_to_sale,
                  transaction_history, comments, followers,
                 following)
        self._event_interested = event_interested
        self._tickets_owned = tickets_owned
=======
    
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


    def add_transaction_history(self, new_transaction: Transaction):
        self._transaction_history.append(new_transaction)

    def remove_transaction_history(self, transaction_to_remove: Transaction):
        if transaction_to_remove in self._purchase_history:
            self._transaction_history.remove(transaction_to_remove)

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

    ## functions

    def sell_ticket(self, ticket, buyer):
        if (buyer.solde<ticket.price):
            print("Solde Insuffisant")
        elif ticket in self.tickets_to_sale and ticket.owner == self:
            transaction = Transaction(self, buyer, ticket.price, ticket)  # No check for sufficient balance
            buyer.solde -= ticket.price
            self.solde += ticket.price
            ticket.owner = buyer
            buyer.tickets_owned.append(ticket)
            self.tickets_to_sale.remove(ticket)
            ticket.availability = False
            print(f"{self.username} sold ticket {ticket.id} to {buyer.username} for {ticket.price}$.")
            return transaction
        else:
            print("Sale impossible. User does not own the ticket or invalid transaction.")

    def display_followers(self):
        if self._followers:
            print(f"{self._username} has the following followers:")
            for follower in self._followers:
                print(f" - {follower}")
        else:
            print(f"{self._username} has no followers.")

    def display_following(self):
        if self._following:
            print(f"{self._username} follows the following people:")
            for user in self._following:
                print(f" - {user}")
        else:
            print(f"{self._username} is not following anyone.")

    def update_bio(self, new_bio: str):
        self._bio = new_bio
        print(f"The biography of {self._username} has been updated.")

    def update_image(self, new_image: str):
        self._image = new_image
        print(f"The profile image of {self._username} has been updated.")

    def add_comment_to_event(self, event: Event, new_comment: Comment):
        if event in self._event_interested:
            event.add_comment(new_comment)
            print(f"{self._username} added a comment to the event: {event.name}")
        else:
            print(f"{self._username} cannot add a comment to an event they are not interested in.")

    def display_comments_on_events(self):
        if self._comments:
            print(f"{self._username}'s comments on events:")
            for comment in self._comments:
                print(f" - {comment.event_name}: {comment.text}")
        else:
            print(f"{self._username} has not made any comments on events.")

class IndividualUser(User):
    def __init__(self, password: str, username: str, email: str, tickets_to_sale: List[Ticket],
                 tickets_owned: List[Ticket], solde: float, color: Colors, comments: List[Comment], image: str, bio: str,
                 event_interested: List[Event], purchase_history: List[Transaction], followers: List[str],
                 following: List[str], date_of_birth: str, address: str):
        super().__init__(password, username, email, tickets_to_sale, solde, color,
                         comments, image, bio, purchase_history, followers, following)
        self._event_interested: List[Event] = event_interested
        self._tickets_owned: List[Ticket] = tickets_owned 
        self._date_of_birth: str = date_of_birth
        self._address: str = address
>>>>>>> faff86e85f2b86df828a8276360025f458c5acf3

    # Additional property and setter for IndividualUser

    @property
    def tickets_owned(self) :
        return self._tickets_owned

    @property
    def event_interested(self):
        return self._event_interested

<<<<<<< HEAD
    @event_interested.setter
    def event_interested(self, new_event_interested):
        self._event_interested = new_event_interested

    def add_event_interested(self, new_event):
        self._event_interested.append(new_event)
=======
    @property
    def tickets_owned(self) -> List[Ticket]:
        return self._tickets_owned

    @date_of_birth.setter
    def date_of_birth(self, new_date_of_birth: str):
        self._date_of_birth = new_date_of_birth

    def add_event_interested(self, new_event: Event):
        self._event_interested.append(new_event)

    def remove_event_interested(self, event_to_remove: Event):
        if event_to_remove in self._event_interested:
            self._event_interested.remove(event_to_remove)

    @address.setter
    def address(self, new_address: str):
        self._address = new_address
    
    @tickets_owned.setter
    def tickets_owned(self, new_tickets_owned):
        self._tickets_owned = new_tickets_owned

>>>>>>> faff86e85f2b86df828a8276360025f458c5acf3

    def remove_event_interested(self, event_to_remove):
        if event_to_remove in self._event_interested:
            self._event_interested.remove(event_to_remove)

    @tickets_owned.setter
    def tickets_owned(self, new_tickets_owned):
        self._tickets_owned = new_tickets_owned

    def add_ticket_owned(self, new_ticket):
        self.tickets_owned.append(new_ticket)

    def remove_ticket_owned(self, ticket_to_remove):
        if ticket_to_remove in self.tickets_owned:
            self.tickets_owned.remove(ticket_to_remove)

    def display_purchase_history(self):
        """
        Display the user's purchase history.
        """
        if self.purchase_history:
            print(f"{self.username} has the following purchase history:")
            for transaction in self.purchase_history:
                print(f" - {transaction}")
        else:
            print(f"{self.username} has no purchase history.")

    def buy_ticket(self, ticket):
        if self.solde >= ticket.price and ticket.availability:
            self.solde -= ticket.price
            ticket.availability = False
            ticket.owner = self
            self.tickets_owned.append(ticket)
            print(f"{self.username} has bought ticket {ticket.id} for the event {ticket.event_name}.")
        else:
            print("Purchase impossible. Insufficient balance or ticket not available.")

    def display_tickets_owned(self):
        if self.tickets_owned:
            print(f"{self.username} owns the following tickets:")
        for ticket in self.tickets_owned:
            print(f" - {ticket.event_name} ({ticket.price} €)")
        else:
            print(f"{self.username} owns no tickets.")

    def add_event_interest(self, new_event):
        """
        Add an event to the user's list of interests.
        """
        self._event_interested.append(new_event)
        print(f"{self.username} is now interested in the event: {new_event.name}")

    def remove_event_interest(self, event_to_remove):
        """
        Remove an event from the user's list of interests.
        """
        if event_to_remove in self._event_interested:
            self.event_interested.remove(event_to_remove)
            print(f"{self.username} is no longer interested in the event: {event_to_remove.name}")

    def display_event_interests(self):
        """
        Display the events that the user is interested in.
        """
        if self._event_interested:
            print(f"{self.username} is interested in the following events:")
            for event in self.event_interested:
                print(f" - {event.name}")
        else:
            print(f"{self.username} has no specific event interests.")

    def display_details(self):
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Balance: {self.solde} €")
        print(f"Color: {self.color}")
        print(f"Bio: {self.bio}")
        print(f"Image: {self.image}")
        print("Tickets for Sale:")
        if self.tickets_to_sale:
            for ticket in self.tickets_to_sale:
                print(f" - Ticket {ticket.id} for {ticket.event['name']} - {ticket.price} €")
        else:
            print("No tickets for sale.")
        print("Event Interests:")
        if self.event_interested:
            for event in self.event_interested:
                print(f" - {event['name']}")
        else:
            print("No specific event interests.")
        print("Followers:")
        if self.followers:
            for follower in self.followers:
                print(f" - {follower.username}")
        else:
            print("No followers.")
        print("Following:")
        if self.following:
            for following_user in self.following:
                print(f" - {following_user.username}")
        else:
            print("Not following anyone.")


class OrganizationUser(User):
<<<<<<< HEAD
    def __init__(self, username, password, email=None,
                  color = "BLACK", image=None, solde=0,  bio=None, tickets_to_sale=[],
                  transaction_history=[], comments=[], followers=[],
                  following=[]):
        super().__init__(username, password, email,
                  color, image, solde,  bio, tickets_to_sale,
                  transaction_history, comments, followers,
                 following)
=======
    def __init__(self, password: str, username: str, email: str, tickets_to_sale: List[Ticket],
                 solde: float, color: Colors, comments: List[Comment], image: str, bio: str,
                 followers: List[str], following: List[str], organization_name: str, registration_number: str):
        super().__init__(password, username, email, tickets_to_sale, solde, color,
                         comments, image, bio, [], followers, following)
        self._organization_name: str = organization_name
        self._registration_number: str = registration_number
>>>>>>> faff86e85f2b86df828a8276360025f458c5acf3

    # Additional property and setter for OrganizationUser

    ### °°° other functions °°°