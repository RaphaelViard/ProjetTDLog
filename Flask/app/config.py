import os

class AppConfig():
    # URI de la base de données SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.getcwd(), 'database.db')
    # Désactiver le suivi des modifications pour améliorer les performances
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Ajoutez ici d'autres paramètres de configuration au besoin
