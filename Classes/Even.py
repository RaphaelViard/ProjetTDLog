from Client import Client

class Ticket:
    def __init__(self,name : str, type : str,salesperson : Client,price : float,location : str):
        self.name = name
        self.type = type
        self.salesperson = salesperson
        self.price = price
        self.location = location


