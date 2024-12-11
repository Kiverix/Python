# Définir une classe Rectangle d'attributs:longueur et largeur et nom et les méthodes:
# perimetre qui retourne le périmètre du rectangle.
# surface qui retourne la surface du rectangle.
# afficher qui affiche le périmètre et la surface d'un rectangle ainsi leurs dimensions en longueur et
# largeur.
# Définir une classe Carre héritant de Rectangle et qui surcharge l’attribut d’instance : nom =
# "carré".
class rectangle():
    def __init__(self, larg=0, long=0):
        self.longueur = long
        self.largeur = larg
        self.nom = "Rectangle"

    def perimetre(self):
        return 2*(self.largeur + self.longueur)

    def surface(self):
        return self.largeur * self.longueur

    def affiche(self):
        print("Type", self.nom)
        print("Perimetre", self.perimetre)
        print("Surface", self.surface)
        print("Dimensions", self.largeur, self.longueur)

class carre(rectangle):
    def __init__(self, c,d):
        super().__init__(c, c)
        self.nom = "carre"

c = carre(5,5)
c.affiche()
