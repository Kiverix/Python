# Écrire un programme python qui permet de définir une classe CompteBancaire, qui permette
# d’instancier des objets tels que compte1, compte2, etc. Le constructeur de cette classe
# initialisera deux attributs d’instance nom et solde, avec les valeurs par défaut ’Doe’ et 1000.
# D’autres méthodes seront définies :
# depot(somme) permettra d’ajouter une certaine somme au solde ;
# retrait(somme) permettra de retirer une certaine somme du solde ;
# affiche() permettra d’afficher le nom du titulaire et le solde de son compte
# transferer(compte) permettra de transférer l’ensemble des informations vers un
# nouveaucompte avec un autre nom. Ce transfert doit engendrer une perte de 3% sur le
# solde

class CompteBancaire:
    def __init__(self, nom="Doe", solde=1000):
        self.nom = nom
        self.solde = solde
    #def depot(somme):
    def affiche():
        print("Compte de: ",self.nom, "solde: ", self.solde)

test = CompteBancaire()
test.affiche()