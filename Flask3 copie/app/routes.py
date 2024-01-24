from flask import render_template, request, redirect, url_for, flash, Response
from flask_login import login_user, login_required, logout_user, current_user
from app import app, db
from app.models import User, Ticket

from datetime import datetime
from flask import jsonify
import secrets
import os
from werkzeug.utils import secure_filename


@app.route("/")
def index():
    return render_template("index.html")


# onglet 1


@app.route("/onglet1", methods=["GET", "POST"])
@login_required
def onglet1():
    if request.method == "POST":
        tri_lieu = request.form.get("tri_lieu")
        tri_date = request.form.get("tri_date")
        tri_nom = request.form.get("tri_nom")
        tri_code = request.form.get("tri_code")
        tickets = Ticket.query.filter(
            Ticket.nomUtilisateur != current_user.username, Ticket.en_vente == True
        ).all()
        if tri_lieu:
            tickets = [
                ticket
                for ticket in tickets
                if tri_lieu.lower() in ticket.lieu_evenement.lower()
            ]
        if tri_date:
            try:
                tri_date = datetime.strptime(tri_date, "%Y-%m-%d").date()
            except ValueError:
                flash(
                    "La date doit être au format a-mm-jj (année-mois-jour).", "danger"
                )
                return redirect(url_for("onglet1"))
            tickets = [
                ticket for ticket in tickets if tri_date == ticket.date_evenement
            ]

        if tri_nom:
            tickets = [
                ticket
                for ticket in tickets
                if tri_nom.lower() in ticket.nom_evenement.lower()
            ]

        if tri_code:
            tickets = [
                ticket
                for ticket in tickets
                if tri_code.lower() == ticket.code_secret.lower()
            ]
    else:
        tickets = Ticket.query.filter(
            Ticket.nomUtilisateur != current_user.username, Ticket.en_vente == True
        ).all()
    return render_template("onglet1.html", tickets=tickets)


# Route pour acheter un ticket
@app.route("/acheter_ticket", methods=["POST"])
@login_required
def acheter_ticket():
    if request.method == "POST":
        ticket_id = request.form.get("ticket_id")
        if ticket_id:
            ticket = Ticket.query.get(ticket_id)
            if ticket and ticket.nomUtilisateur != current_user.username:
                acheteur = User.query.filter_by(username=current_user.username).first()
                vendeur = User.query.filter_by(username=ticket.nomUtilisateur).first()
                if acheteur and vendeur:
                    prix_ticket = ticket.prix_ticket
                    if acheteur.money >= prix_ticket:
                        acheteur.money -= prix_ticket
                        vendeur.money += prix_ticket
                        ticket.nomUtilisateur = acheteur.username
                        ticket.en_vente = False
                        db.session.commit()
                        flash("Achat du ticket réussi !", "success")
                        return redirect(url_for("onglet1"))
                    else:
                        return render_template("solde_insuffisant.html")
            else:
                flash("Le ticket sélectionné n'est pas disponible.", "danger")
                return jsonify({"status": "error"})
        else:
            flash("Erreur lors de l'achat du ticket.", "danger")
            return jsonify({"status": "error"})

    return jsonify({"status": "error"})


## onglet 2


@app.route("/onglet2", methods=["GET", "POST"])
@login_required
def onglet2():
    if current_user.is_authenticated:
        if request.method == "POST":
            nom_evenement = request.form.get("nomEvenement")
            date_evenement = request.form.get("dateEvenement")
            lieu_evenement = request.form.get("lieuEvenement")
            prix_ticket = request.form.get("prixTicket")

            new_ticket = Ticket(
                nom_evenement=nom_evenement,
                date_evenement=date_evenement,
                lieu_evenement=lieu_evenement,
                prix_ticket=prix_ticket,
                nomUtilisateur=current_user.username,
                en_vente=True,  # Le ticket est en vente
            )
            db.session.add(new_ticket)
            db.session.commit()
            flash("Le ticket a été mis en vente avec succès !", "success")
            return redirect(url_for("onglet2"))
        return render_template("onglet2.html")
    else:
        flash("Veuillez vous connecter pour accéder à Onglet 2", "danger")
        return redirect(url_for("connexion"))


def generate_unique_code():
    while True:
        code_secret = secrets.token_urlsafe(16)
        existing_ticket = Ticket.query.filter_by(
            code_secret=code_secret
        ).first()  # On vérifie que le code secret n'existe pas déjà dans la base de donnée
        if not existing_ticket:
            return code_secret


# Route pour mettre en vente un ticket
@app.route("/mettre_en_vente", methods=["POST"])
@login_required
def mettre_en_vente():
    if request.method == "POST":
        nom_evenement = request.form.get("nomEvenement")
        date_evenement_str = request.form.get("dateEvenement")
        lieu_evenement = request.form.get("lieuEvenement")
        prix_ticket = request.form.get("prixTicket")
        if (
            not nom_evenement
            or not date_evenement_str
            or not lieu_evenement
            or not prix_ticket
        ):
            flash("Veuillez remplir tous les champs obligatoires.", "danger")
            return redirect(url_for("onglet2"))
        try:
            date_evenement = datetime.strptime(date_evenement_str, "%Y-%m-%d").date()
        except ValueError:
            flash(
                "Le format de la date est incorrect. Utilisez le format YYYY-MM-DD.",
                "danger",
            )
            return redirect(url_for("onglet2"))
        code_secret = generate_unique_code()
        uploaded_file = request.files["file"]
        if uploaded_file.filename != "":
            filename = secure_filename(uploaded_file.filename)
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            uploaded_file.save(file_path)
        else:
            file_path = None
        new_ticket = Ticket(
            nom_evenement=nom_evenement,
            date_evenement=date_evenement,
            lieu_evenement=lieu_evenement,
            prix_ticket=prix_ticket,
            nomUtilisateur=current_user.username,
            code_secret=code_secret,
            chemin_pdf=file_path,
        )
        db.session.add(new_ticket)
        db.session.commit()
        flash("Le ticket a été mis en vente avec succès !", "success")
        return redirect(url_for("onglet2"))
    return redirect(url_for("onglet2"))


## onglet 3


@app.route("/onglet3")
@login_required
def onglet3():
    if current_user.is_authenticated:
        tickets_en_vente = Ticket.query.filter(
            (Ticket.nomUtilisateur == current_user.username) & (Ticket.en_vente == True)
        ).all()
        tickets_achetes = Ticket.query.filter(
            (Ticket.nomUtilisateur == current_user.username)
            & (Ticket.en_vente == False)
        ).all()
        return render_template(
            "onglet3.html",
            tickets_en_vente=tickets_en_vente,
            tickets_achetes=tickets_achetes,
        )
    else:
        flash("Veuillez vous connecter pour accéder à Onglet 3", "danger")
        return redirect(url_for("connexion"))


@app.route("/download_pdf/<int:ticket_id>")
@login_required
def download_pdf(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    if not ticket or ticket.nomUtilisateur != current_user.username:
        flash("Vous n'avez pas accès à ce ticket.", "danger")
        return redirect(url_for("onglet3"))
    if not ticket.chemin_pdf:
        flash("Aucun PDF associé à ce ticket.", "danger")
        return redirect(url_for("onglet3"))
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], ticket.chemin_pdf)

    def generate():
        with open(file_path, "rb") as pdf_file:
            while True:
                chunk = pdf_file.read(1024)
                if not chunk:
                    break
                yield chunk

    response = Response(generate(), content_type="application/pdf")
    response.headers[
        "Content-Disposition"
    ] = f"inline; filename={secure_filename(ticket.chemin_pdf)}"
    return response


@app.route("/mettre_a_jour_solde", methods=["POST"])
@login_required
def mettre_a_jour_solde():
    if request.method == "POST":
        nouveau_solde = float(request.form["nouveauSolde"])
        user = User.query.filter_by(id=current_user.id).first()
        user.money += nouveau_solde
        db.session.commit()
        flash("Solde mis à jour avec succès !", "success")
        return redirect(url_for("onglet3"))
    else:
        flash("Utilisateur introuvable.", "danger")
        return redirect(url_for("onglet3"))


@app.route("/mettre_a_jour_Bio", methods=["POST"])
@login_required
def mettre_a_jour_Bio():
    if request.method == "POST":
        nouvelle_bio = request.form["NouvelleBio"]
        user = User.query.filter_by(id=current_user.id).first()
        user.Bio = nouvelle_bio
        db.session.commit()
        flash("Bio mise à jour avec succès !", "success")
        return redirect(url_for("onglet3"))
    else:
        flash("Utilisateur introuvable.", "danger")
        return redirect(url_for("onglet3"))


@app.route("/check_username", methods=["POST"])
def check_username():
    data = request.get_json()
    username = data["username"]
    user = User.query.filter_by(username=username).first()
    if user:
        response = {"usernameExists": True}
    else:
        response = {"usernameExists": False}
    return jsonify(response)


@app.route("/PageUser/<nom_utilisateur>", methods=["GET"])
@login_required
def PageUser(nom_utilisateur):
    Utilisateur = User.query.filter_by(username=nom_utilisateur).first()
    tickets = Ticket.query.filter_by(nomUtilisateur=Utilisateur.username, en_vente=True)
    if Utilisateur:
        return render_template(
            "PageUser.html", Utilisateur=Utilisateur, tickets=tickets
        )


@app.route("/supprimer_ticket/<int:ticket_id>", methods=["POST"])
def supprimer_ticket(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    if ticket:
        db.session.delete(ticket)
        db.session.commit()
    return redirect("/onglet3")


@app.route("/remettre_vente/<int:ticket_id>", methods=["POST"])
def remettre_vente(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    if ticket:
        ticket.en_vente = True
        db.session.commit()
        return jsonify({"message": "Ticket remis en vente avec succès"}), 200
    else:
        return jsonify({"error": "Ticket non trouvé"}), 404


@app.route("/retirer_vente/<int:ticket_id>", methods=["POST"])
def retirer_vente(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    if ticket:
        ticket.en_vente = False
        db.session.commit()
    return redirect(url_for("onglet3"))


@app.route("/modifier_vente", methods=["POST"])
def modifier_vente():
    if request.method == "POST":
        ticket_id = request.form.get("ticket_id")
        nouveau_nom = request.form.get("nomEvenementModif")
        nouveau_lieu = request.form.get("lieuEvenementModif")
        date_evenement_str = request.form.get("dateEvenementModif")
        nouvelle_date = datetime.strptime(date_evenement_str, "%Y-%m-%d")
        nouveau_prix = request.form.get("prixTicketModif")
        ticket = Ticket.query.get(ticket_id)
        if ticket:
            ticket.nom_evenement = nouveau_nom
            ticket.lieu_evenement = nouveau_lieu
            ticket.date_evenement = nouvelle_date
            ticket.prix_ticket = nouveau_prix
            db.session.commit()
    return redirect(url_for("onglet3"))


@app.route("/mettre_a_jour_mot_de_passe", methods=["POST"])
@login_required
def mettre_a_jour_mot_de_passe():
    if request.method == "POST":
        nouveau_mot_de_passe = request.form["nouveauMotDePasse"]
        current_user.password = nouveau_mot_de_passe
        db.session.commit()
        flash("Mot de passe mis à jour avec succès.", "success")
    return redirect(url_for("onglet3"))


# login


@app.route("/inscription", methods=["GET", "POST"])
def inscription():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        Bio = request.form["Bio"]
        new_user = User(username=username, password=password, Bio=Bio, money=0)
        db.session.add(new_user)
        db.session.commit()
        flash("Inscription réussie ! Vous pouvez maintenant vous connecter.", "success")
        return redirect(url_for("connexion"))
    return render_template("inscription.html")


@app.route("/connexion", methods=["GET", "POST"])
def connexion():
    if request.method == "POST":
        username = request.form["username"]
        Password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user and user.password == Password:
            login_user(user)
            flash("Connexion réussie !", "success")
            return redirect(url_for("index"))
        flash(
            "La connexion a échoué. Veuillez vérifier votre nom d'utilisateur.",
            "danger",
        )
    return render_template("connexion.html")


@app.route("/deconnexion")
@login_required
def deconnexion():
    logout_user()
    flash("Vous avez été déconnecté.", "info")
    return render_template("deconnexion.html")
