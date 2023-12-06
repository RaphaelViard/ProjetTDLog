class Event:
<<<<<<< HEAD
    def __init__(self, name, date, place, duration, info=None, category=None, image=None, tickets=[], comments=[]):
=======
    def __init__(self, name, date, place, duration, info="None", category="None", image=None, tickets=[], comments=[]):
>>>>>>> faff86e85f2b86df828a8276360025f458c5acf3
        self._name = name
        self._place = place
        self._image = image
        self._info = info
        self._category = category
        self._duration = duration  # float nb hours
        self._date = date # type Date
        self._tickets = tickets  # List of Ticket objects
        self._comments = comments  # List of Comment objects

    ## property / setter

    @property
    def name(self):
        return self._name

    @property
    def duration(self):
        return self._duration

    @property
    def date(self):
        return self._date

    @property
    def place(self):
        return self._place

    @property
    def category(self):
        return self._category

    @property
    def image(self):
        return self._image

    @property
    def info(self):
        return self._info

    @property
    def tickets(self):
        return self._tickets

    @property
    def comments(self):
        return self._comments

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @duration.setter
    def duration(self, new_duration):
        self._duration = new_duration

    @date.setter
    def date(self, new_date):
        self._date = new_date

    @place.setter
    def place(self, new_place):
        self._place = new_place

    @image.setter
    def image(self, new_image):
        self._image = new_image

    @category.setter
    def category(self, new_category):
        self._category = new_category

    @info.setter
    def info(self, new_info):
        self._info = new_info

    @tickets.setter
    def tickets(self, new_tickets):
        self._tickets = new_tickets

    @comments.setter
    def comments(self, new_comments):
        self._comments = new_comments

    ## display

    def display_event_info(self):
        print(f"Event: {self.name}")
        print(f"Date: {self.date.to_string()}")
        print(f"Place: {self.place.place}")
        print(f"Available Tickets: {len(self.tickets)}")
        print(f"Nb comments: {len(self.comments)}")

    ## operation

    def update_event_info(self, new_info):
        self._info = new_info

    ## comment

    def add_comment(self, new_comment):
        self._comments.append(new_comment)

    def remove_comment(self, comment_to_remove):
        if comment_to_remove in self.comments:
            self.comments.remove(comment_to_remove)

    def get_total_comments(self):
        return len(self.comments)

    def get_comments_by_user(self, username):
        # Get comments made by a specific user
        return [comment for comment in self.comments if comment.username == username]

    def has_comments(self):
        # Check if there are comments for the event
        return bool(self.comments)

    ## ticket

    def add_ticket(self, new_ticket):
        self.tickets.append(new_ticket)

    def remove_ticket(self, ticket_to_remove):
        if ticket_to_remove in self.tickets:
            self.tickets.remove(ticket_to_remove)

    def sell_ticket(self, num_tickets):
        if num_tickets <= len(self.tickets):
            sold_tickets = self.tickets[:num_tickets]
            self.tickets = self.tickets[num_tickets:]
            return sold_tickets
        else:
            print("Not enough available tickets.")

    # availability

    def get_available_tickets_count(self):
        # Get the count of available tickets
        return sum(1 for ticket in self.tickets if ticket.availability)

    def has_tickets_with_availability(self):
        # Check if there are still tickets available for the event
        return any(ticket.availability for ticket in self.tickets)

    def is_sold_out(self):
        # Check if all tickets for the event are sold out
        return all(not ticket.availability for ticket in self.tickets)

    # price

    def find_tickets_by_price_range(self, min_price, max_price):
        matching_tickets = [ticket for ticket in self.tickets if min_price <= ticket.price <= max_price]
        return matching_tickets

    def sort_tickets_by_price(self, reverse=False):
        self._tickets.sort(key=lambda ticket: ticket.price, reverse=reverse)

    def get_average_ticket_price(self):
        if not self.tickets:
            return 0
        total_price = sum(ticket.price for ticket in self.tickets)
        average_price = total_price / len(self.tickets)
        return average_price


    def get_ticket_price_range(self):
        # Get the minimum and maximum prices of available tickets
        if not self.tickets:
            return (0, 0)
        prices = [ticket.price for ticket in self.tickets]
        return min(prices), max(prices)

    def calculate_total_revenue(self):
        # Calculate the total revenue generated from ticket sales
        return sum(ticket.price for ticket in self.tickets if not ticket.availability)

    def get_tickets_by_category_and_price_range(self, category, min_price, max_price):
        # Get tickets within a specific category and price range
        return [ticket for ticket in self.tickets
                if ticket.category == category and min_price <= ticket.price <= max_price]

    def get_tickets_with_max_price(self, max_price):
        # Get tickets with a price below or equal to the specified maximum price
        return [ticket for ticket in self.tickets if ticket.price <= max_price]

    # owner

    def get_tickets_by_owner(self, owner_username):
        # Get tickets owned by a specific user
        return [ticket for ticket in self.tickets if ticket.owner and ticket.owner.username == owner_username]

    def find_tickets_by_owner_and_availability(self, owner_username, available=True):
        # Find tickets owned by a specific user with optional availability filter
        return [ticket for ticket in self.tickets
                if ticket.owner and ticket.owner.username == owner_username and ticket.availability == available]

    def find_tickets_by_owner_username(self, owner_username):
        # Find tickets owned by a specific user
        return [ticket for ticket in self.tickets if ticket.owner and ticket.owner.username == owner_username]

    ### °°° other functions °°°






