# Import des classes depuis les fichiers correspondants
from Ticket import Ticket
from Transac import Transaction
from Event import Event
from Date import Date
from Com import Comment
from Place import Place
from User import User, IndividualUser, OrganizationUser
import datetime
""""
# Création d'instances d'événements
event1 = Event(1, "Concert", "2023-12-31", "Stadium", "City", "Description for Concert","Rock",2)
event2 = Event(2, "Festival", "2023-11-15", "Park", "City", "Description for Festival","Pop",3)

# Création d'instances d'utilisateurs individuels
user1 = IndividualUser("pass1", "user1", "user1@example.com", [], [], 100.0, "BLUE", [], "image1.jpg", "Bio for User 1",
                       [event1], [], [], [], "1990-01-01", "123 Main St")

user2 = IndividualUser("pass2", "user2", "user2@example.com", [], [], 50.0, "RED", [], "image2.jpg", "Bio for User 2",
                       [event2], [], [], [], "1985-05-20", "456 Oak St")

# Création d'une instance d'utilisateur organisation
org_user = OrganizationUser("orgpass", "orguser", "orguser@example.com", [], 200.0, "YELLOW", [], "org_image.jpg",
                             "Description for Organization User", [], [], "Music Org", "ORG12345")

# Création d'instances de tickets
ticket1 = Ticket(101, event1, 20.0,user1)
ticket2 = Ticket(102, event2, 30.0,user2)

# Utilisation des méthodes pour vendre et acheter des tickets
transaction = Transaction(user1, user2, 25.0,ticket1)
transaction.execute_transaction()

# Affichage des informations des utilisateurs
user1.display_tickets_owned()
user2.display_tickets_owned()

# Affichage des informations des transactions
print("Transaction Summary:")
print(transaction.get_transaction_summary())

# Affichage des commentaires sur les événements
comment1 = Comment(10,user1, "wow","Great concert!", Date("june"))
comment2 = Comment(10,user2, "wow","Exciting festival!",Date("june"))
event1.add_comment(comment1)
event2.add_comment(comment2)

print("Event Comments:")
event1.display_comments()

# (Vous pouvez ajouter plus d'opérations en fonction de votre logique métier)
"""
#Création de dates
ListDates = []
for i in range(1, 367):  # L'année 2024 a 366 jours car c'est une année bissextile
    date = datetime.date(2024, 1, 1) + datetime.timedelta(days=i - 1)
    date_formattee = date.strftime("%d-%m-%Y")
    ListDates.append(Date(date_formattee))

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
    tickets = []  # Liste de Ticket fictive
    comments = []  # Liste de Comment fictive
    category = "Concert" if i % 2 == 0 else "Match"
    duration = i/5  # Durée fictive pour tous les événements en heure
    nouvel_event = Event(name, date, place, image, info, tickets, comments, category, duration)
    ListEvents.append(nouvel_event)

# ListEvents[5].display_event_info()

User1 = IndividualUser("azerty","Pingouin06","Pingouin@gmail.com",[],[],50,"BLUE",[],"image1.jpg","J'aime le Rap et les match du PSG",[],[],[],[],"15-04-1998","Rue Victor Hugo Paris")
User2 = IndividualUser("12345","Serpent27","Serpent@gmail.com",[],[],80,"RED",[],"image2.jpg","J'aime le raggae et les match du Racing95",[],[],[],[],"15-08-1996","Rue Voltaire Marseille")
User3 = OrganizationUser("AGoodPassword","AccorArena","Accor@arena.fr",[],0,"ORANGE",[],"image3.jpg","Salle de concert située vers Gare de Lyon",[],[],"Accor Hotel Arena","021")

#Trucs a chaner pour les users : Orga n'a pas de ticket_owned, difference orga_name et username ? EventInterested ne devrait exister que pour individual

Ticket1 = Ticket("01",ListEvents[5],30,User3)
Ticket2 = Ticket("02",ListEvents[6],40,User3)
Ticket3 = Ticket("03",ListEvents[3],50,User3)
Tickets = [Ticket1,Ticket2,Ticket3]
for Tick in Tickets:
    User3.add_ticket_to_sale(Tick)
#Rajouter dans un ticket : Event : pour un ticket, on est "obligés" de rjaouter l'attribut Event pour avoir toutes les infos du concert
#Ajouter les events dans les dates, les events dans les Places, et les tickets dans les bons events
k=0
for Ev in ListEvents:
    for Tick in Tickets:
        if Ev==Tick.event:
            Ev.add_ticket(Tick) #ON rajoute les tickets dans les bons Events
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

date_test = Date("04-12-2023","15:30",ListEvents[:2])
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