from pattern import inp
def matrix(c):
    mat1=[]
    print("Enter your matrix %d"%(c))
    p=r[0]
    while p>0:
        s = input()
        d=[]
        for i in s:
            if i!=' ':
                f=int(i,10)
                d.append(f)
        p-=1
        mat1.append(d)
    return mat1
mat3=[]
a=input("Enter the size of your matrix 1\n")
r = inp(a)
mat1=matrix(1)
a=input("Enter the size of your matrix 2\n")
r = inp(a)
mat2=matrix(2)
for i in range(r[0]):
    d=[]
    for j in range(r[1]):
        s=mat1[i][j]-mat2[i][j]
        d.append(s)
    mat3.append(d)
print("Your matrix is")
for i in range(r[0]):
    for j in range(r[1]):
        print("%d  "%mat3[i][j],end=" ")
    print("\n")