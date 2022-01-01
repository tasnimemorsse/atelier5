class Point:


    def __init__(self, x=0.0, y=0.0):    

        self.x1 = float(x)
        self.y1 = float(y)


class Segment:


    def __init__(self, a1, b1, a2, b2):

        self.orig = Point(a1, b1)
        self.extrem = Point(a2, b2)
    def display(self):
        print("[(",self.orig.x1,",", self.orig.y1,")", "(",self.extrem.x1,"," ,self.extrem.y1,")]")



Se = Segment(1, 2, 3, 4)
Se.display()