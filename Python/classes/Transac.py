class Transaction:
    def __init__(self, acheteur, vendeur, montant, produit):
        self.acheteur = acheteur
        self.vendeur = vendeur
        self.montant = montant
        self.produit = produit

    def afficher_details(self):
        print(f"Transaction: {self.acheteur.username} a payé {self.montant} à {self.vendeur.username} pour {self.produit}.")


#Ajouter fctn transaction possible ? 