class Triangle:
    def __init__(self):
       self.side1=int(input("give a lenth of first variable"))
       self.side2=int(input("give a lenth of second variable"))
       self.side3=int(input("give a lenth of third variable"))
def read_triangle():
    b=Triangle
    return b
def is_triangle():
    c=Triangle.sort()
    if c.get(0)+c.get(1)>c.get(2):
        print("valid triangle",read_triangle(Triangle))
    else:
        print("invalid triangle")