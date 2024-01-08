from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from app import app, db
from app.models import User, Ticket
from datetime import datetime
from flask import jsonify,send_from_directory
from io import BytesIO
import secrets

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/onglet2', methods=['GET', 'POST'])
@login_required
def onglet2():
    if current_user.is_authenticated:
        if request.method == 'POST':
            nom_evenement = request.form.get('nomEvenement')
            date_evenement = request.form.get('dateEvenement')
            lieu_evenement = request.form.get('lieuEvenement')
            prix_ticket = request.form.get('prixTicket')

            new_ticket = Ticket(
                nom_evenement=nom_evenement,
                date_evenement=date_evenement,
                lieu_evenement=lieu_evenement,
                prix_ticket=prix_ticket,
                nomUtilisateur=current_user.username,
                en_vente=True  # Le ticket est en vente
            )
            db.session.add(new_ticket)
            db.session.commit()

            flash('Le ticket a été mis en vente avec succès !', 'success')

            # Redirigez l'utilisateur vers Onglet 2 après la mise en vente
            return redirect(url_for('onglet2'))

        return render_template('onglet2.html')
    else:
        flash('Veuillez vous connecter pour accéder à Onglet 2', 'danger')
        return redirect(url_for('connexion'))

@app.route('/onglet3')
@login_required
def onglet3():
    if current_user.is_authenticated:
        # Récupérez les tickets en vente par l'utilisateur actif depuis la base de données
        tickets_en_vente = Ticket.query.filter(
            (Ticket.nomUtilisateur == current_user.username) & (Ticket.en_vente == True)
        ).all()

        # Récupérez les tickets achetés par l'utilisateur actif depuis la base de données
        tickets_achetes = Ticket.query.filter(
            (Ticket.nomUtilisateur == current_user.username) & (Ticket.en_vente == False)
        ).all()

        return render_template('onglet3.html', tickets_en_vente=tickets_en_vente, tickets_achetes=tickets_achetes)
    else:
        # Rediriger vers la page de connexion si l'utilisateur n'est pas connecté
        flash('Veuillez vous connecter pour accéder à Onglet 3', 'danger')
        return redirect(url_for('connexion'))


# Route d'inscription
@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        Bio = request.form['Bio']

        # Créez un nouvel utilisateur et ajoutez-le à la base de données
        new_user = User(username=username, password=password,Bio=Bio,money=0)
        db.session.add(new_user)
        db.session.commit()

        # Après l'inscription réussie, redirigez l'utilisateur vers la page de connexion
        flash('Inscription réussie ! Vous pouvez maintenant vous connecter.', 'success')
        return redirect(url_for('connexion'))  # Redirection vers la page de connexion

    return render_template('inscription.html')

@app.route('/connexion', methods=['GET', 'POST'])
def connexion():
    if request.method == 'POST':
        username = request.form['username']

        # Vérifiez si l'utilisateur existe dans la base de données (vous devrez implémenter cette logique)
        user = User.query.filter_by(username=username).first()
        if user: 
            # L'utilisateur est connecté avec succès
            login_user(user)  # Enregistrez l'utilisateur connecté

            flash('Connexion réus sie !', 'success')

            # Redirigez l'utilisateur vers la page d'accueil (index)
            return redirect(url_for('index'))

        flash('La connexion a échoué. Veuillez vérifier votre nom d\'utilisateur.', 'danger')

    return render_template('connexion.html')

# Route de déconnexion
@app.route('/deconnexion')
@login_required
def deconnexion():
    logout_user()
    flash('Vous avez été déconnecté.', 'info')
    return render_template('deconnexion.html')


codes_and_files = {}

@app.route('/mettre_en_vente', methods=['POST'])
@login_required
def mettre_en_vente():
    if request.method == 'POST':
        # Récupérez les données du formulaire
        nom_evenement = request.form.get('nomEvenement')
        date_evenement_str = request.form.get('dateEvenement')  # Obtenez la date sous forme de chaîne de caractères
        lieu_evenement = request.form.get('lieuEvenement')
        prix_ticket = float(request.form.get('prixTicket'))
        date_evenement = datetime.strptime(date_evenement_str, '%Y-%m-%d').date()
        code_secret = secrets.token_urlsafe(16)

        new_ticket = Ticket(
            nom_evenement=nom_evenement,
            date_evenement=date_evenement,
            lieu_evenement=lieu_evenement,
            prix_ticket=prix_ticket,
            nomUtilisateur=current_user.username,
            code_secret=code_secret
            )
        db.session.add(new_ticket)
        db.session.commit()

        uploaded_files = request.files.getlist('file')
        for file in uploaded_files:
            if file.filename != '':
                filename = secrets.secure_filename(file.filename)
                codes_and_files[code_secret] = filename
      

        flash('Le ticket a été mis en vente avec succès !', 'success')
        return redirect(url_for('onglet2'))

    return redirect(url_for('onglet2'))

@app.route('/telecharger_fichier/<code_secret>', methods=['GET'])
@login_required
def telecharger_fichier(code_secret):
    if code_secret in code_and_files:
        filename = code_and_files[code_secret]

        # Ici, vous devriez avoir le chemin complet vers le fichier à télécharger
        # Assurez-vous d'avoir le chemin approprié vers votre répertoire de téléchargement
        chemin_fichier = f'/chemin/vers/repertoire/telechargement/{filename}'
        
        return send_file(chemin_fichier, as_attachment=True)
    else:
        flash('Fichier introuvable', 'danger')
        return redirect(url_for('onglet3'))


# Route pour récupérer les tickets mis en vente par l'utilisateur actif au format JSON
@app.route('/tickets_en_vente', methods=['GET'])
@login_required
def tickets_en_vente():
    if current_user.is_authenticated:
        # Récupérez les tickets en vente par l'utilisateur actif depuis la base de données
        tickets = Ticket.query.filter_by(en_vente=True, nomUtilisateur=current_user.username).all()

        # Créez une liste de dictionnaires pour les tickets en vente par l'utilisateur actif
        tickets_en_vente = []
        for ticket in tickets:
            ticket_info = {
                'nom_evenement': ticket.nom_evenement,
                'date_evenement': str(ticket.date_evenement),
                'lieu_evenement': ticket.lieu_evenement,
                'prix_ticket': ticket.prix_ticket,
            }
            tickets_en_vente.append(ticket_info)

        # Renvoyez les tickets en vente par l'utilisateur actif au format JSON
        return jsonify(tickets_en_vente)
    else:
        # Rediriger vers la page de connexion si l'utilisateur n'est pas connecté
        flash('Veuillez vous connecter pour accéder à cette page', 'danger')
        return redirect(url_for('connexion'))

@app.route('/tickets_recommandes', methods=['GET'])
@login_required
def tickets_recommandes():
    if current_user.is_authenticated:
        # Récupérez les tickets recommandés depuis la base de données
        tickets_recommandes = Ticket.query.filter(
            Ticket.nomUtilisateur != current_user.username
        ).all()

        # Créez une liste de dictionnaires pour les tickets recommandés
        tickets_data = []
        for ticket in tickets_recommandes:
            ticket_info = {
                'nom_evenement': ticket.nom_evenement,
                'date_evenement': str(ticket.date_evenement),
                'lieu_evenement': ticket.lieu_evenement,
                'prix_ticket': ticket.prix_ticket,
            }
            tickets_data.append(ticket_info)

        # Renvoyez les tickets recommandés au format JSON
        return jsonify(tickets_data)
    else:
        # Rediriger vers la page de connexion si l'utilisateur n'est pas connecté
        flash('Veuillez vous connecter pour accéder à cette page', 'danger')
        return redirect(url_for('connexion'))

@app.route('/acheter_ticket', methods=['POST'])
@login_required
def acheter_ticket():
    if request.method == 'POST':
        ticket_id = request.form.get('ticket_id')
        if ticket_id:
            ticket = Ticket.query.get(ticket_id)
            if ticket and ticket.nomUtilisateur != current_user.username:
                acheteur = User.query.filter_by(username=current_user.username).first()
                vendeur = User.query.filter_by(username=ticket.nomUtilisateur).first()
                if acheteur and vendeur:
                    prix_ticket=ticket.prix_ticket
                    if acheteur.money >= prix_ticket:
                        acheteur.money -= prix_ticket
                        vendeur.money += prix_ticket
                        ticket.nomUtilisateur = acheteur.username
                        ticket.en_vente = False
                        db.session.commit()
                        flash('Achat du ticket réussi !', 'success')
                        return redirect(url_for('onglet1'))
                    else:
                         return render_template('solde_insuffisant.html')   
            else:
                flash('Le ticket sélectionné n\'est pas disponible.', 'danger')
                return jsonify({"status": "error"})
        else:
            flash('Erreur lors de l\'achat du ticket.', 'danger')
            return jsonify({"status": "error"})

    return jsonify({"status": "error"})

@app.route('/liste_tickets')
def nouvelle_page():
    tickets = Ticket.query.all()
    return render_template('liste_tickets.html',tickets=tickets)

@app.route('/onglet1', methods=['GET', 'POST'])
@login_required
def onglet1():
    if current_user.is_authenticated:
        if request.method == 'POST':
            tri_lieu = request.form.get('tri_lieu')
            tri_date = request.form.get('tri_date')
            tri_nom = request.form.get('tri_nom')

            # Récupérez tous les tickets non triés par défaut
            tickets = Ticket.query.filter(Ticket.nomUtilisateur != current_user.username, Ticket.en_vente == True).all()

            # Appliquez la logique de filtrage en fonction des informations saisies par l'utilisateur
            if tri_lieu:
                tickets = [ticket for ticket in tickets if tri_lieu.lower() in ticket.lieu_evenement.lower()]

            if tri_date:
                # Convertissez la date entrée au format "a-mm-jj" en objet datetime
                try:
                    tri_date = datetime.strptime(tri_date, '%Y-%m-%d').date()
                except ValueError:
                    # Gestion de l'erreur si la date n'est pas au bon format
                    return "La date doit être au format a-mm-jj (année-mois-jour)."

                # Filtrer les tickets en fonction de la date
                tickets = [ticket for ticket in tickets if tri_date == ticket.date_evenement]

            if tri_nom:
                tickets = [ticket for ticket in tickets if tri_nom.lower() in ticket.nom_evenement.lower()]

        else:
            # Si la méthode est GET (affichage initial), récupérez tous les tickets non triés
            tickets = Ticket.query.filter(Ticket.nomUtilisateur != current_user.username, Ticket.en_vente == True).all()

        return render_template('onglet1.html', tickets=tickets)
    else:
        flash('Veuillez vous connecter pour accéder à Onglet 2', 'danger')
        return redirect(url_for('connexion'))

# Route pour mettre à jour le solde
@app.route('/mettre_a_jour_solde', methods=['POST'])
@login_required
def mettre_a_jour_solde():
    if request.method == 'POST':
        nouveau_solde = float(request.form['nouveauSolde'])

        # Recherchez l'utilisateur actuel dans la base de données
        user = User.query.filter_by(id=current_user.id).first()
        user.money += nouveau_solde
        # Enregistrez les modifications dans la base de données
        db.session.commit()

        flash('Solde mis à jour avec succès !', 'success')
        return redirect(url_for('onglet3'))  # Redirection vers l'onglet 3 après la mise à jour du solde
    else:
        flash('Utilisateur introuvable.', 'danger')
        return redirect(url_for('onglet3'))

@app.route('/mettre_a_jour_Bio', methods=['POST'])
@login_required
def mettre_a_jour_Bio():
    if request.method == 'POST':
        nouvelle_bio = request.form['NouvelleBio']

        # Recherchez l'utilisateur actuel dans la base de données
        user = User.query.filter_by(id=current_user.id).first()
        user.Bio = nouvelle_bio
        # Enregistrez les modifications dans la base de données
        db.session.commit()

        flash('Bio mise à jour avec succès !', 'success')
        return redirect(url_for('onglet3'))  # Redirection vers l'onglet 3 après la mise à jour du solde
    else:
        flash('Utilisateur introuvable.', 'danger')
        return redirect(url_for('onglet3'))


@app.route('/check_username', methods=['POST'])
def check_username():
    data = request.get_json()
    username = data['username']

    user = User.query.filter_by(username=username).first()

    if user:
        response = {'usernameExists': True}
    else:
        response = {'usernameExists': False}

    return jsonify(response)

@app.route('/PageUser/<nom_utilisateur>',methods=['GET'])
@login_required
def PageUser(nom_utilisateur):
      Utilisateur = User.query.filter_by(username=nom_utilisateur).first()
      tickets = Ticket.query.filter_by(nomUtilisateur=Utilisateur.username)
      if Utilisateur:
            return render_template('PageUser.html', Utilisateur=Utilisateur,tickets=tickets) 

@app.route('/Retirervente',methods=['POST'])
@login_required
def Retirervente():
    ticket_id = request.form['ticket_id']
    ticket= Ticket.query.filter_by(id=ticket_id).first()
    ticket.en_vente = False
    db.session.commit()
    return redirect(url_for('onglet3'))

@app.route('/mettrevente',methods=['POST'])
@login_required
def mettrevente():
    ticket_id = request.form['ticket_id']
    prix = float(request.form['prix'])
    ticket= Ticket.query.filter_by(id=ticket_id).first()
    if ticket:
        ticket.en_vente = True
        ticket.prix_ticket = prix
        db.session.commit()
        return redirect(url_for('onglet3'))

  
@app.route('/Retirersite',methods=['POST'])
@login_required
def Retirersite():
    ticket_id = request.form['ticket_id']
    ticket= Ticket.query.filter_by(id=ticket_id).first()
    if ticket:
        db.session.delete(ticket)
        db.session.commit()
        return redirect(url_for('onglet3'))

@app.route('/Changerprix',methods=['POST'])
@login_required
def Changerprix():
    ticket_id = request.form['ticket_id']
    nouveau_prix = float(request.form['nouveau_prix'])
    ticket= Ticket.query.filter_by(id=ticket_id).first()
    if ticket:
        ticket.prix_ticket = nouveau_prix
        db.session.commit()
        return redirect(url_for('onglet3'))

  




