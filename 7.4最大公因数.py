a=int(input('enter the first number'))
b=int(input('enter the second number'))
if a>b:
    while a%b!=0:
        x=a%b
        a=b
        b=x
        print(b)
if a<b:
    while a%b!=0:
        x=b%a
        b=a
        a=x
        print(a)