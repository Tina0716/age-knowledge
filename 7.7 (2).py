def my_search(A,B):
    if A in B:
        print (B.index(A))
    else:
        return (-1,"item not found")

A=int(input("enter an number"))
B=[3,4,5,7]
print(my_search(A,B))