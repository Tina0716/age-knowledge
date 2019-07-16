class student:
    def __init__(self):
        self.name=''
        self.ID=0
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
a=student()
a.readfromkeyboard()
print()
a.get_all_student_from_keyboard()
a.find_GPA()
a.print_student()