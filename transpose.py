a=input("Enter the size of your matrix\n")
r=[]
for i in a:
    if i!=' ':
        t=int(i,10)
        r.append(t)
mat1=[]
mat2=[]
print("Enter your matrix 1")
for i in range(r[0]):
    d=[]
    for j in range(r[1]):
        s=int(input())
        d.append(s)
    mat1.append(d)
