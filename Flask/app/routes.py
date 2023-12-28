from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from app import app, db
from app.models import User, Ticket
from datetime import datetime
from flask import jsonify

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

        # Créez un nouvel utilisateur et ajoutez-le à la base de données
        new_user = User(username=username, password=password,money=0)
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

@app.route('/mettre_en_vente', methods=['POST'])
@login_required
def mettre_en_vente():
    if request.method == 'POST':
        # Récupérez les données du formulaire
        nom_evenement = request.form.get('nomEvenement')
        date_evenement_str = request.form.get('dateEvenement')  # Obtenez la date sous forme de chaîne de caractères
        lieu_evenement = request.form.get('lieuEvenement')
        prix_ticket = float(request.form.get('prixTicket'))

        # Convertissez la chaîne de caractères en objet date
        date_evenement = datetime.strptime(date_evenement_str, '%Y-%m-%d').date()

        # Créez un nouveau ticket et associez-le à l'utilisateur actif
        new_ticket = Ticket(
            nom_evenement=nom_evenement,
            date_evenement=date_evenement,
            lieu_evenement=lieu_evenement,
            prix_ticket=prix_ticket,
            nomUtilisateur=current_user.username
        )
        db.session.add(new_ticket)
        db.session.commit()

        flash('Le ticket a été mis en vente avec succès !', 'success')

    return redirect(url_for('onglet2'))

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
                        return redirect(url_for('index'))
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

        # Afficher la page d'Onglet 1 si l'utilisateur est connecté
        if request.method == 'POST':
            # Récupérer les critères de recherche depuis le formulaire
            nom_evenement = request.form.get('nomEvenement')
            date_evenement = request.form.get('dateEvenement')
            lieu_evenement = request.form.get('lieuEvenement')
            # Requête à la base de données pour les tickets correspondants
            tickets_search = Ticket.query.filter_by(
                nom_evenement=nom_evenement,
                date_evenement=date_evenement,
                lieu_evenement=lieu_evenement,
                nomUtilisateur=current_user.username  # Assurez-vous de filtrer les tickets de l'utilisateur actif
            ).all()

            # Chargez les tickets recommandés depuis la base de données
            tickets_recommandes = Ticket.query.filter(
                (Ticket.nomUtilisateur != current_user.username) & (Ticket.en_vente == True)
            ).all()

            return render_template('onglet1.html', tickets_search=tickets_search, tickets_recommande=tickets_recommandes)

        # Chargez les tickets recommandés depuis la base de données pour l'affichage
        tickets_recommandes = Ticket.query.filter(
            Ticket.nomUtilisateur != current_user.username  # Exclure les tickets de l'utilisateur actif
        ).all()

        return render_template('onglet1.html', tickets_recommandes=tickets_recommandes)
    else:
        # Rediriger vers la page de connexion si l'utilisateur n'est pas connecté
        flash('Veuillez vous connecter pour accéder à Onglet 1', 'danger')
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
        
