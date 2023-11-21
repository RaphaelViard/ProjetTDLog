# models.py

from django.db import models

class ProfilUtilisateur(models.Model):
    nom = models.CharField(max_length=100)
    numero_telephone = models.CharField(max_length=15)
    # Autres champs pertinents

    def __str__(self):
        return self.nom

class Evenement(models.Model):
    nom = models.CharField(max_length=255)
    date = models.DateTimeField()
    lieu = models.CharField(max_length=255)
    # Autres champs pertinents

    def __str__(self):
        return self.nom

class Ticket(models.Model):
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    vendeur = models.ForeignKey(ProfilUtilisateur, on_delete=models.CASCADE)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    categorie = models.CharField(max_length=50)
    quantite_disponible = models.PositiveIntegerField()
    # Autres champs pertinents

    def __str__(self):
        return f"{self.evenement} - {self.categorie}"

class Achat(models.Model):
    acheteur = models.ForeignKey(ProfilUtilisateur, on_delete=models.CASCADE)
    tickets = models.ManyToManyField(Ticket)
    date_achat = models.DateTimeField(auto_now_add=True)
    montant_total = models.DecimalField(max_digits=10, decimal_places=2)
    # Autres champs pertinents

    def __str__(self):
        return f"{self.acheteur} - {self.date_achat}"

class Commentaire(models.Model):
    auteur = models.ForeignKey(ProfilUtilisateur, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE, null=True, blank=True)
    achat = models.ForeignKey(Achat, on_delete=models.CASCADE, null=True, blank=True)
    # Autres champs pertinents

    def __str__(self):
        return f"{self.auteur} - {self.date_creation}"
