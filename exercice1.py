class vecteur2D:


    def __init__(self, x=0, y=0): 

        self.x1 = x 
        self.y1 = y

    def display(self):
        print(self.x1,self.y1)


v=vecteur2D()
v1=vecteur2D(4,6)
print("Constructeur sans parametres par defaut= ")
v.display()
print("Constructeur avec parametres par defaut= ")
v1.display()


