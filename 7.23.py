import sys
class Employee:
    def __init__(self):
        self.first_name=''
        self.last_name=''
        self.eID=0
        self.e_duration=0
        self.salary_per_day=0
    def readfromkeyboard(self,firstname,lastname,eID,e_duration,salaryperday):
        self.first_name=firstname
        self.last_name=lastname
        self.eID=int(eID)
        self.e_duration=int(e_duration)
        self.salary_per_day=int(salaryperday)
    def __str__(self):
        return ('name:%s %s\neID:%d\ne_duration:%d\nreceived salary:%d'%(self.first_name,self.last_name,self.eID,self.e_duration,self.received_payment()))
    def received_payment(self):
        return(self.e_duration*self.salary_per_day)
f=open('input.py')
for i in f:
    print(i)

my_input=open('input.py','r')
orig_stdout=sys.stdout
my_output=open('output.py','w')
sys.stdout=my_output
total=0
for i in my_input:
    currentE=Employee()
    info=i.strip().split(',')
    currentE.readfromkeyboard(info[0],info[1],info[2],info[3],info[4])
    print(currentE)
    total=total+currentE.received_payment()
print(my_output,'total amount payments of all stuff is:$',total)
my_input.close()
sys.stdout=orig_stdout
my_output.close()