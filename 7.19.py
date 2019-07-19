class student:
    def __init__(self):
        self.name=''
        self.ID=0
    def readfromkeyboard(self):
        while(True):
            try:
                self.name=input("enter a name of student")
                self.ID=int(input("enter the ID"))
                return
            except:
                print('wrong value,please try again')

    def print_student(self):
        print(self.name,self.ID)
    def __eq__(self, other):
        if self.name==other.name and self.ID==other.ID:
            return True
        else:
            return False
    def __str__(self):
        return('%s %d'%(self.name,self.ID))


list=[]
for i in range(3):
    s1=student()
    s1.readfromkeyboard()
    flag=False
    for s in list:
        flag=True
    if (flag==False):
        list.append(s1)
for i in list:
    print(list)