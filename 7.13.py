class Triangle:
    def __init__(self):
       self.side1=0
       self.side2=0
       self.side3=0

    def read_triangle(self):
        self.side1=float((input("give a lenth of first variable")))
        self.side2=float((input("give a lenth of second variable")))
        self.side3=float((input("give a lenth of third variable")))

    def is_triangle(self):
        T=False
        if (self.side1>self.side2+self.side3):
            if (self.side2>self.side1+self.side3):
                if (self.side3 > self.side1 + self.side2):
                    T=True
                    print('this is valid')
        else:
            print('this is not valid triangle')
        return T
t1=Triangle()
t1.read_triangle()
t1.is_triangle()