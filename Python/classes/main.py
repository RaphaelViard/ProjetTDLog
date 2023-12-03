# Import des classes depuis les fichiers correspondants
from Ticket import Ticket
from Transac import Transaction
from Event import Event
from Date import Date
from Com import Comment
from User import User, IndividualUser, OrganizationUser

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
