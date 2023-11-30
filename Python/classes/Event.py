from Ticket import Ticket

class Event:
    def __init__(self, name, date, location, image, info, available_tickets, hour, comments):
        self._name = name
        self._date = date
        self._location = location
        self._image = image
        self._info = info
        self._hour = hour
        self._available_tickets = available_tickets
        self._comments = comments

    ## property / setter

    @property
    def name(self):
        return self._name

    @property
    def date(self):
        return self._date

    @property
    def location(self):
        return self._location

    @property
    def image(self):
        return self._image

    @property
    def info(self):
        return self._info

    @property
    def hour(self):
        return self._hour

    @property
    def available_tickets(self):
        return self._available_tickets

    @property
    def comments(self):
        return self._comments

    @name.setter
    def set_name(self, new_name):
        self._name = new_name

    @date.setter
    def set_date(self, new_date):
        self._date = new_date

    @location.setter
    def set_location(self, new_location):
        self._location = new_location

    @image.setter
    def set_image(self, new_image):
        self._image = new_image

    @info.setter
    def set_info(self, new_info):
        self._info = new_info

    @hour.setter
    def set_hour(self, new_hour):
        self._hour = new_hour

    @available_tickets.setter
    def set_available_tickets(self, new_available_tickets):
        self._available_tickets = new_available_tickets

    @comments.setter
    def set_comments(self, new_comments):
        self._comments = new_comments

    ## other functions

    def add_ticket(self, new_ticket):
        self._available_tickets.append(new_ticket)

    def remove_ticket(self, ticket_to_remove):
        if ticket_to_remove in self._available_tickets:
            self._available_tickets.remove(ticket_to_remove)

    def add_comment(self, new_comment):
        self._comments.append(new_comment)

    def remove_comment(self, comment_to_remove):
        if comment_to_remove in self._comments:
            self._comments.remove(comment_to_remove)

    ### °°° other functions °°°
