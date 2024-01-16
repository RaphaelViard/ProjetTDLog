# run.py

from app import app, db

if __name__ == '__main__':
    # Créez les tables dans la base de données
    with app.app_context():
        db.create_all()
    app.run(debug=True)
