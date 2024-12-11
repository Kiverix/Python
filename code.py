#Making a Class
class Etudiant:
    def __init__(self):
        print("Saisir votre nom:")
        self.nom = input()
        print("Saisir votre prenom")
        self.prenom = input()

#    def __init__(self,nm:" ",pr:" "):
#        if nm=="" and pr=="":
#            print("Saisir votre nom")
#            self.nom = input()
#            print("Saisire votre prenom")
#            self.prenom = input()
#        else:
#            self.nom = nm
#            self.prenom = pr

    def bonjour():
        print("Je suis ",self.nom," ",self.prenom)

bob = Etudiant()
bob.nom = "Michel"
#brayan = Etudiant('Dupont',"Paul")
#print(brayan.__dict__)
bob.bonjour()