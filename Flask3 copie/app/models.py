from app import db
from flask_login import UserMixin
from sqlalchemy import Column, String

# from app import db
# from flask_login import UserMixin
# from app import login_manager
# from sqlalchemy import ForeignKeyConstraint, Column, Integer, String, Boolean, Float
# import datetime
# from sqlalchemy.ext.declarative import declarative_base


# Modèle de données pour la classe User
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    Bio = db.Column(db.String(9999))
    money = db.Column(db.Float)

    def __repr__(self):
        return f"<User {self.username}>"


# Modèle de données pour la classe Ticket
class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code_secret = db.Column(db.String(32), unique=True)
    nom_evenement = db.Column(db.String(255))
    date_evenement = db.Column(
        db.Date
    )  # Assurez-vous que le nom de la colonne est "date_evenement"
    lieu_evenement = db.Column(db.String(255))
    prix_ticket = db.Column(db.Float)
    nomUtilisateur = db.Column(db.String(255))
    en_vente = db.Column(db.Boolean, default=True)
    chemin_pdf = Column(String)

    def __repr__(self):
        return f"<Ticket {self.nom_evenement}>"
