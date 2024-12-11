#Écrire un programme Python qui permet de définir une classe Satellite qui permette d’instancier
#des objets simulant des satellites artificiels lancés dans l’espace, autour de la terre. Le
#constructeur de cette classe initialisera les attributs d’instance suivants, avec les valeurs par
#défaut indiquées : masse = 100, vitesse = 0.
#Créez plusieurs satellites avec des valeurs différentes.
#Ajoutez deux méthodes accélérer/ralentir permettant de modifier automatiquement la vitesse
#du satellite. LA vitesse maximale du satellite est définit comme étant égale au triple de sa masse. 

class satellite:
    def __init__(sat,mss=100,vel=0):
        if mss=="" and vel=="":
            print("Masse du Satellite:")
            sat.mss = int(input())
            print("Vitesse du satellite:")
            sat.vel = int(input())
        else:
            sat.mss = mss
            sat.vel = vel
    def DeltaV():
        print("Changer la vitesse:")
        sat.vel = int(input())
        

sputnik = satellite(785, 46)
hubble = satellite(953, 754)
luna1 = satellite(547, 98)
surveyor = satellite()

hubble.DeltaV()

print(sputnik.__dict__)
print(hubble.__dict__)
print(luna1.__dict__)
print(surveyor.__dict__)