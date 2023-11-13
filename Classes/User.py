from typing import Literal
from Ticket import Ticket

Colors = Literal["RED", "BLUE", "ORANGE", "BROWN", "PURPLE ", "YELLOW", "WHITE", "BLACK"]


class User:
    def __init__(self : str,password : str,username : str,email : str,ticketstosale : list[Ticket],ticketowned : list[Ticket], money : float, color : Colors):
        self._password = password
        self.username = username
        self.email = email
        self.ticketstosale = ticketstosale #The tickets we are trying to sell
        self.ticketowned = ticketowned #The tickets we own (!= tickets we sell)
        self.money = money #Money the user has on his account
        self.color = color


    @property.setter
    def password(self,newpassword):
        self._password = newpassword


