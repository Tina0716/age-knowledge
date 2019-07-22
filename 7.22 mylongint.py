class mylongint:
    def __init__(self):
        self.mylongint_number=0
    def read(self):
        self.mylongint_number=int(input('enter a number'))
    def __str__(self):
        return 'my longlist number:%d'%self.mylongint_number

    def __add__(self, other):
        addvalue=self.mylongint_number+other.mylongint_number
        print('addition result',addvalue)

    def __sub__(self,other):
        subvalue=self.mylongint_number-other.mylongint_number
        print('subtraction',subvalue)
my1=mylongint()
my2=mylongint()
my1.read()
my2.read()
print(my1)
print(my2)
a=my1+my2
b=my1-my2