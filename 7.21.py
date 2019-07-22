class Rectangle:
    def __init__(self):
        self.width=0
        self.hight=0
    def __str__(self):
        return ('this is a rectangle,the width is %d hight is %d'%(self.width,self.hight))
    def area_perimeter(self):
        area=self.width*self.hight
        perimeter=2*self.width+2*self.hight
        return (area,perimeter)
    def get_width(self):
        self.width=int(input('enetr the width'))
        if self.width<=0:
            raise ValueError('Invalid width')

    def get_hight(self):
        self.hight=int(input('enter the hight'))
        if self.hight<=0:
            raise ValueError('Invalid hight')

    def __eq__(self, other):
        if (self.width==other.width and self.hight==other.hight) or (self.width==other.hight and self.hight==other.width):
            return True
        else:
            return False
my_list=[]
user_input=''
while user_input!='q':
    for i in range(2):
        try:
            rec1=Rectangle()
            rec1.get_width()
            rec1.get_hight()
            v=rec1.area_perimeter()
            my_list.append(rec1)
            print(rec1)
            print('area:%d\nperimeter:%d'%(v[0],v[1]))
        except ValueError as excpt:
            print(excpt)
            print('could not calculate')
        user_input=input('enter any key(q to quit)')
r1=Rectangle()
r1.get_width()
r1.get_hight()
r2=Rectangle()
r2.get_width()
r2.get_hight()
if r1==r2:
    print('two rectangles are the same')