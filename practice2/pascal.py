n=int(input("Enter the number of rows\n"))
a=[]
def add(x,y):
    return x+y
for i in range(n):
    a.append([])
    a[i].append([1])

    for j in range(1,i):
        a[i].append(list(map(add,a[i-1][j-1],a[i-1][j])))
    if n!=0:
        a[i].append([1])
for i in a:
    print(i)
for i in range(n):
    print(" "*(n-i),end=" ",sep="  ")
    for j in range(0,i+1):
        print((a[i][j][0]),end=" ",sep="  ")
    print()

