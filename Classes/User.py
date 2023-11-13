from typing import Literal
from Ticket import Ticket

Colors = Literal["RED", "BLUE", "ORANGE", "BROWN", "PURPLE ", "YELLOW", "WHITE", "BLACK"]


class Client:
    def __init__(self : str,password : str,username : str,email : str,nbtickets : int,tickets : list[Ticket], money : float, color : Colors):
        self._password = password
        self.username = username
        self.email = email
        self.nbtickets = nbtickets  #The number of tickets we are trying to sell
        self.tickets = tickets #The tickets we are trying to sell
        self.money = money #Money the user on his account
        self.color = color


    @property.setter
    def password(self,newpassword):
        return self._password
