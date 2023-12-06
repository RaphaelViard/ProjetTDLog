"""

### --- Test Viard ---

# Import des classes depuis les fichiers correspondants
from Ticket import Ticket
from Event import Event
from Date import Date,DateEvent
from Place import Place
from User import IndividualUser, OrganizationUser
import datetime

#Création de dates
ListDates = []
for i in range(1, 367):  # L'année 2024 a 366 jours car c'est une année bissextile
    date = datetime.date(2024, 1, 1) + datetime.timedelta(days=i - 1)
    date_formattee = date.strftime("%d-%m-%Y")
    ListDates.append(DateEvent(date_formattee))

# Affichage des dix premières dates pour exemple

for i in range(10):
    ListDates[i].__str__()

# Création de 20 Places différentes
ListPlaces = []
for i in range(50):
    place_name = f"Country_{i}%City_{i}%Adress_{i}"
    nouvelle_place = Place(place_name, [])
    ListPlaces.append(nouvelle_place)


#Création d'événements
ListEvents = []
for i in range(10):
    name = f"Event_{i}"
    date = ListDates[3*i+7]  # Date fictive pour tous les événements
    place = ListPlaces[2*i]
    image = f"image_{i}.jpg"
    info = f"Information about Event_{i}"
<<<<<<< HEAD
    category = "Concert" if i % 2 == 0 else "Match"
    duration = i/5  # Durée fictive pour tous les événements en heure
    nouvel_event = Event(name=name, date=date, place=place, duration=duration, image=image, info=info, category=category)
=======
    tickets = []  # Liste de Ticket fictive
    comments = []  # Liste de Comment fictive
    category = "Concert" if i % 2 == 0 else "Match"
    duration = i/5  # Durée fictive pour tous les événements en heure
    nouvel_event = Event(name, date, place, image, info, tickets, comments, category, duration)
>>>>>>> faff86e85f2b86df828a8276360025f458c5acf3
    ListEvents.append(nouvel_event)

# ListEvents[5].display_event_info()

User1 = IndividualUser(password="azerty",username="Pingouin06",email="Pingouin@gmail.com",solde=50,color="BLUE",image="image1.jpg",bio="J'aime le Rap et les match du PSG")
User2 = IndividualUser(password="12345",username="Serpent27",email="Serpent@gmail.com",solde=80,color="RED",image="image2.jpg",bio="J'aime le raggae et les match du Racing95")
User3 = OrganizationUser(password="AGoodPassword",username="AccorArena",email="Accor@arena.fr",solde=0,color="ORANGE",image="image3.jpg",bio="Salle de concert située vers Gare de Lyon")

#Trucs a chaner pour les users : Orga n'a pas de ticket_owned, difference orga_name et username ? EventInterested ne devrait exister que pour individual

Ticket1 = Ticket("01",ListEvents[5],30,User3)
Ticket2 = Ticket("02",ListEvents[6],40,User3)
Ticket3 = Ticket("03",ListEvents[3],50,User3)
<<<<<<< HEAD
TicketsL = [Ticket1,Ticket2,Ticket3]

for Tick in TicketsL:
    User3.add_ticket_to_sale(Tick)
#Rajouter dans un ticket : Event : pour un ticket, on est "obligés" de rjaouter l'attribut Event pour avoir toutes les infos du concert
=======
Tickets = [Ticket1,Ticket2,Ticket3]
for Tick in Tickets:
    User3.add_ticket_to_sale(Tick)
#Rajouter dans un ticket : Event : pour un ticket, on est "obligés" de rjaouter l'attribut Event pour avoir toutes les infos du concert 
>>>>>>> faff86e85f2b86df828a8276360025f458c5acf3
#Ajouter les events dans les dates, les events dans les Places, et les tickets dans les bons events
k=0
for Ev in ListEvents:
    for Tick in TicketsL:
        if Ev==Tick.event:
            Ev.add_ticket(Tick) #On rajoute les tickets dans les bons Events
            k +=1

print(k)
j=0
#On ajoute ensuite tous les évenements aux dates
for D in ListDates:
    for i in range(len(ListEvents)):
        if D.date == ListEvents[i].date.date:
            j += 1
            D.add_event(ListEvents[i])
print(j)
l=0
for P in ListPlaces:
    for i in range(len(ListEvents)):
        if P.place==ListEvents[i].place.place:
            l += 1
            P.add_event(ListEvents[i])
print(l)

##

date_test = DateEvent("04-12-2023","15:30",ListEvents[:2])
print(date_test.__str__())

#On donne les 3 tickets a OrganizationUser(user3)

User1.display_event_interests()
User1.add_event_interest(ListEvents[5])
User1.display_event_interests()
print(ListEvents[5]._tickets[0].event.name)

#Quand quelqu'un devient possesseur d'un ticket : Changer le owner dans ticket,
#  enlever le ticket si il est dans une liste spéciale (Event si il n'est plus a vendre)
#  et le rajouter dans la bonne liste, changer son availability,
#  Ajouter transaction dans purchase History
#Ici, les 3 tickets sont a User3, User1 va en acheter 2.
#sell_ticket : change les solde, les owners

Transaction1 = User3.sell_ticket(Ticket1,User1)

User1.solde += 50

Transaction2 = User3.sell_ticket(Ticket2,User1)

<<<<<<< HEAD
"""

### --- Test ChatGPT ---

from datetime import datetime
from Ticket import Ticket
from Com import Comment
from Transac import Transaction
from User import User, IndividualUser, OrganizationUser

# Création d'utilisateurs
user1 = IndividualUser(username="JohnDoe", password="password1", solde=100)
user2 = IndividualUser(username="JaneSmith", password="password2", solde=150)
organization = OrganizationUser(username="EventOrg", password="eventpassword", solde=0)

# Création d'événements
event1 = {"name": "Concert", "date": "2023-12-31"}
event2 = {"name": "Conference", "date": "2023-11-15"}

# Création de tickets
ticket1 = Ticket(id=1, event=event1, price=50, owner=user1)
ticket2 = Ticket(id=2, event=event2, price=30, owner=user2)

# Ajout de tickets à la vente
user1.add_ticket_to_sale(ticket1)
user2.add_ticket_to_sale(ticket2)

# Affichage des tickets à la vente
print(f"{user1.username}'s tickets for sale:")
for ticket in user1.tickets_to_sale:
    print(f" - Ticket {ticket.id} for {ticket.event['name']}")

# Achat d'un ticket
buyer = user2
transaction = user1.sell_ticket(ticket1, buyer)
buyer.add_transaction_history(transaction)

# Affichage de l'historique des transactions de l'acheteur
print(f"{buyer.username}'s transaction history:")
for transaction in buyer.transaction_history:
    print(f" - Transaction {transaction.seller.username} -> {transaction.buyer.username}: {transaction.price}€")

# Ajout de commentaires
comment1 = Comment(author=user1, title="Great Event!", content="I enjoyed the concert.", rating=2, date=datetime.now())
comment2 = Comment(author=user2, title="Informative", content="The conference was very informative.", rating=1, date=datetime.now())

# Ajout de commentaires à un événement
event1_comments = []
event1_comments.append(comment1)
event1_comments.append(comment2)

# Affichage des commentaires sur un événement
print(f"Comments on {event1['name']}:")
for comment in event1_comments:
    print(f" - {comment.author.username}: {comment.title} - {comment.content}")

# Mise à jour de la bio et de l'image d'un utilisateur
user1.update_bio("New bio for JohnDoe.")
user1.update_image("new_profile_pic.jpg")

# Affichage des détails de l'utilisateur
user1.display_details()

# Affichage des événements auxquels l'utilisateur est intéressé
user1.display_event_interests()



=======
>>>>>>> faff86e85f2b86df828a8276360025f458c5acf3
