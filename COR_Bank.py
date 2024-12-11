class CompteBancaire:
    def __init__(self, n="Doe", s=1000):
        self.nom = n
        self.montant = s
    def depot(self, montant):
        if(montant>0):
            self.montant += montant 
            # self.montant n'est pas la mème chose que montant alors ils peuvent avoire le meme nom
    def retrait(self, montant):
        if(self.montant >= montant and montant>0):
            self.montant-=montant
    def affiche(self):
        print(self.nom, " : ", self.montant)
    def transferer(self):
        destinataire = CompteBancaire()
        destinataire.nom = self.nom
        destinataire.montant = self.montant * 0.97
        return destinataire
    def comparer(self, cautre):
        return self.nom == cautre.nom and self.montant == cautre.montant

c1 = CompteBancaire("bob",123456)
c1.affiche()
c1.depot(33333)
c1.affiche()
c1.retrait(123456)
c1.affiche()
c2 = c1.transferer()
c2.affiche()
print(c1.comparer(c2))
