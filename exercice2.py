class vecteur2D:


    def __init__(self, x=0, y=0): 

        self.x1 = x  
        self.y1 = y

    def display(self):
        print(self.x1,self.y1)

    def __add__(self, vect):

        v1=self.x1+vect.x1
        v2=self.y1+vect.y1
        print("la somme des deux vecteurs  ",v1,v2)


v=vecteur2D(1,5)
print("le premier vecteur  ")
v.display()

v1=vecteur2D(3,2)
print("le deuxieme vecteur  " )
v1.display()

v3=v+v1



