print("We will find the roots of ax^2+bx+c=0")
a=int(imput("the first index a is"))
b=int(imput("the second index b is"))
c=int(imput("the third index c is"))

p= b^2-4*a*c
if p>0:
   delter=math.sqrt(p)
   root1=(-b+delter)/(2*a)
   root2=(-b-delter)/(2*a)
   print("There are two different solusions,the first on is",root1,"the second one is",root2 )
elif p==0:
    delter=math.sqrt(p)
    root=(-b)/(2*a)
    print("There is one solusion,the root is",root)
else: print("There is no real solution")
