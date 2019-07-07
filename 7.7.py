print("Give a list of numers")
L=[1,25,6,3,4]
L2=[]
def my_sort(L):
    i=len(L)
    while i>0:
        a=min(L)
        L2.append(a)
        L.remove(a)
        i=i-1
    return L2

print(my_sort(L))