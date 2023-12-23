# run.py

from app import app, db
from app.models import User, Ticket  # Importez vos modèles ici

if __name__ == '__main__':
    # Créez les tables dans la base de données
    with app.app_context():
        db.create_all()
    app.run(debug=True)
