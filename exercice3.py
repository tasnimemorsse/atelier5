class rectangle:
    def __init__(self,longueur=3,largeur=2):
        self.lon=longueur
        self.lar=largeur
        self.Nom="rectangle"
    def display(self):
      print("la surface  ",self.Nom,": ",self.lon*self.lar)

class carre(rectangle):
    def __init__(self,nu=3):
        self.num=nu
        rectangle.__init__(self, nu, nu)
        self.Nom = "carré"
    def display(self):
        print(self.Nom, ":  ", self.num * self.num)





rec=rectangle(2,4)
rec.display()
ca=carre()
ca.display()