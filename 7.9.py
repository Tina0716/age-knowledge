j_p={}
j_n=int(input())
j_r=int(input())
lst=[]
while 0<j_r<10 and 0<=j_n<100:
    j_p[j_n]=j_r
    j_n=int(input())
    j_r=int(input())
else:
    print("out of range")
for i in j_p:
    lst.append(i)
    b=lst.sort()
print("play number is %d and the rate is %d"%[b,j_p(b)])