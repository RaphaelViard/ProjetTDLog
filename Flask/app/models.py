from app import app
from app import db
from flask_login import UserMixin
from app import login_manager  # Import login_manager from app
from sqlalchemy import ForeignKeyConstraint
import datetime

# Modèle de données pour la classe User
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    money = db.Column(db.Float)

    def __repr__(self):
        return f'<User {self.username}>'

# Modèle de données pour la classe Ticket
class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom_evenement = db.Column(db.String(255))
    date_evenement = db.Column(db.Date)  # Assurez-vous que le nom de la colonne est "date_evenement"
    lieu_evenement = db.Column(db.String(255))
    prix_ticket = db.Column(db.Float)
    nomUtilisateur = db.Column(db.String(255))
    en_vente = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Ticket {self.nom_evenement}>'



with app.app_context():
    db.create_all()
    for i in range(10):
        ticket_existant = Ticket.query.filter_by(nom_evenement=f"evenement {i}").first()
        if not ticket_existant:
            nouveau_ticket = Ticket(nom_evenement=f"evenement {i}",
            date_evenement=datetime.date(2023, 12, 31),
            lieu_evenement=f"Lieu {i}",
            prix_ticket=50.0,
            nomUtilisateur=f"Utilisateur {i}",
            en_vente=True)
            db.session.add(nouveau_ticket)
            db.session.commit()
            print("Ticket ajouté !")