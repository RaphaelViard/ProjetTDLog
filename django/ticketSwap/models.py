from django.db import models

class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    price = models.FloatField()
    availability = models.BooleanField(default=True)
    owner = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Ticket {self.id} - {self.event.name}"

class Transaction(models.Model):
    seller = models.ForeignKey('User', related_name='transactions_sold', on_delete=models.CASCADE)
    buyer = models.ForeignKey('User', related_name='transactions_bought', on_delete=models.CASCADE)
    price = models.FloatField()
    ticket = models.ForeignKey('Ticket', on_delete=models.CASCADE)

    def __str__(self):
        return f"Transaction {self.id}"

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    solde = models.FloatField(default=0)
    color = models.CharField(max_length=50, default="BLACK")
    image = models.ImageField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    tickets_to_sale = models.ManyToManyField('Ticket', blank=True)
    comments = models.ManyToManyField('Comment', blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, blank=True)
    following = models.ManyToManyField('self', symmetrical=False, blank=True)
    transaction_history = models.ManyToManyField('Transaction', blank=True)

    def __str__(self):
        return self.username

class IndividualUser(User):
    event_interested = models.ManyToManyField('Event', blank=True)
    tickets_owned = models.ManyToManyField('Ticket', blank=True)

    def __str__(self):
        return f"IndividualUser: {self.username}"

class OrganizationUser(User):
    def __str__(self):
        return f"OrganizationUser: {self.username}"

class Date(models.Model):
    date = models.CharField(max_length=255)
    hour = models.CharField(max_length=255)

    def __str__(self):
        return f"date : {self.date} - hour : {self.hour}"

class DateEvent(Date):
    event = models.ManyToManyField('Event', blank=True)

class Place(models.Model):
    place = models.CharField(max_length=255)
    event = models.ManyToManyField('Event', blank=True)

    def __str__(self):
        return f"place : {self.place}"

class Event(models.Model):
    name = models.CharField(max_length=255)
    # Add other event-related fields as needed

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"Comment by {self.user.username} on {self.event.name}"
