

class Client:
    def __init__(self,password,username,email,nbtickets,tickets,money,color):
        self._password = password
        self.username = username
        self.email = email
        self.nbtickets = nbtickets
        self.tickets = tickets
        self.money = money
        self.color = color


    @property.setter
    def password(self,newpassword):
        return self._password
    
a=0
        