#Making a Class
class Etudiant:
#    def __init__(self):
#        print("Saisir votre nom:")
#        self.nom = input()
#        print("Saisir votre prenom")
#        self.prenom = input()

    def __init__(self,nm:" ",pr:" "):
        self.nom = nm
        self.prenom = pr

bob = Etudiant()
bob.nom = "Michel"
brayan = Etudiant('Dupont',"Paul")
print(brayan.__dict__)