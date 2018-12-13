a=input("Enter size of matrix 1 \n")
def inp(r):
    w = len(r)
    d = []
    for i in range(w):
        if a[i] == ' ':
            continue
        else:
            d.append(r[i])
    return d
d=inp(a)
list1 = []
w = int(d[0], 10)
x = int(d[1], 10)
for i in range(w):
    r = []
    for j in range(x):
        d=int(input("Enter your matrix\n"))
        r.append(d)
    list1.append(r)
a=input("Enter size of matrix 2 \n")
w=len(a)
d=[]
for i in range(w):
    if a[i]==' ':
        continue
    else:
        d.append(a[i])
list2=[]
w=int(d[0],10)
x=int(d[1],10)
for i in range(w):
    r = []
    for j in range(x):
        d=int(input("Enter your matrix\n"))
        r.append(d)
    list2.append(r)
list3=[]
for i,j in list1,list2 :
    r = []
    for l, k in i, j:
        l=int(l,10)
        k=int(k,10)
        s=l+k
        r.append(str(s))
    list3.append(r)

for r in list3:
    for l in r:
        print("%d "%l,end=" ")
    print("\n")