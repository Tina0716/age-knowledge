class student:
    def __init__(self):
       self.name=''
       self.age=0
       self.grades=[]
       self.GPA=0
       self.graduation_day=0
       self.graduation_month=0
       self.graduation_year=0

    def read_student(self):
        self.name=input("enter a name of student")
        self.age=int(input("enter a number of age"))
        self.grades=int(input["enter a list of grades"])
        self.graduation_day=int((input("enter the graduation day")))
        self.graduation_month=int((input("enter the graduation month")))
        self.graduation_year=int((input("enter the graduation year")))
    def find_GPA(self):
        a=0
        for i in self.grades:
            sum=a+i
        self.GPA=sum/len(self.grades)

s1=student()
print(s1.read_student())
print(s1.find_GPA())
