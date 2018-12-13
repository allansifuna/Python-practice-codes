a=input("Enter a text\n")
c=[]
d=len(a)
a[::-1]
for i in range(d):
    h=['!','@','#','$','%','^','&','*','(',')','_','-','=','+',';',':','"',',','.','/','?','<','>']
    if a[i]==' 'or a[i]in(h):
        continue
    else:
        c.append(str(a[i]))
e=set(c)
e=sorted(e)
c=sorted(c)
for s in e:
    count=0
    for z in c:
        if s==z:
            count+=1
        else:
            continue
    v=print("%c-%d"%(s.upper(),count))
print(v)