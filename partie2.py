class Etudiant :
    def __init__(self,nom,prenom,age,cne,moyenne):
        self.nom=nom
        self.prenom=prenom
        self.age=age
        self.cne=cne
        self.moyenne=moyenne
mylist = [
Etudiant("kholoud","rett",22,"G12346h",18),
Etudiant("oumaima","alali",12,"7655hgds",10),
Etudiant("tasnim","yanis",24,"P13112178",20),


]


mylist.sort(key=lambda Etudiant:Etudiant.age )

print("la liste trier selon l'age  ")
for i in mylist :
    print(i.nom,i.prenom,i.age,i.cne,i.moyenne)

mylist.sort(key=lambda Etudiant:Etudiant.moyenne)
print("la liste trier selon le moyenne  ")
for i in mylist :
    print(i.nom,i.prenom,i.age,i.cne,i.moyenne)