class satellite:
    def __init__(self, m=100, v=0):
        self.masse = m
        self.vitesse = v
        
    def accélérer(self):
        self.vitesse += 10
        if self.vitesse > 3*self.masse:
            self.vitesse = 3*self.masse

    def ralentire(self):
        self.vitesse -= 10
        if vitesse < 0:
            self.vitesse = 0

s1 = satellite()
i=0

while i < 100:
    s1.accélérer()
    i+=1

print(s1.__dict__)