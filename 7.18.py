class student:
    def __init__(self):
        self.name=''
        self.ID=0
        self.name2=''
        self.ID2=0
        self.GPA=0.0
    def readfromkeyboard(self):
        self.name=input("enter a name of student")
        self.ID=int(input("enter the ID"))
    def get_all_student_from_keyboard(self):
        global student_list
        student_list=[]
        for i in range(10):
            s1=int(input('enter grade'))
            student_list.append(s1)
        return student_list
    def find_GPA(self):
        self.GPA=sum(student_list)/10

    def print_student(self):
        print(self.name,self.ID,self.GPA)
    def __lt__(self, other):
        if self.GPA<other.GPA:
            return True
        else:
            return False
    def __gt__(self, other):
        if self.GPA>other.GPA:
            return True
        else:
            return False
    def __eq__(self, other):
        if self.name==other.name and self.ID==other.ID:
            return True
        else:
            return False
student1=student()
student1.readfromkeyboard()
print()
student1.get_all_student_from_keyboard()
student1.find_GPA()
student1.print_student()
student2=student()
student2.readfromkeyboard()
print()
student2.get_all_student_from_keyboard()
student2.find_GPA()
student2.print_student()
print(student1.__lt__(student2))