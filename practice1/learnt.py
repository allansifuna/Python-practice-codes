def dict(l):
    v=set(l)
    v=list(v)
    di={}
    for i in v:
        count=0
        for j in l:
            if i==j:
                count+=1
            else:
                continue
        di[i]=count

    return di.items
a=input("Enter any name or letters\n")
d=[]
for i in a:
    if i!=' ':
        d.append(str(i))
    else:
        continue
di=dict(d)
print(di)