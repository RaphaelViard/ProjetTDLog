from Client import Client

class Ticket:
    def __init__(self,name : str,type,salesperson,price,location):
        self.name = name
        self.type = type
        self.salesperson = salesperson
        self.price = price
        self.location = location
