import string,random
def pass_gen(g):
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    all=string.printable
    digits=string.digits
    passw=''
    pass_list1=[]
    pass2=[]
    pass_list=[]
    l=random.randint(0,25)
    u=random.randint(0,25)
    d=random.randint(0,8)
    c=random.randint(0,3)
    for i in range(20):
        l = random.randint(0, 25)
        u = random.randint(0, 25)
        d = random.randint(0, 8)
        pass_list1.append(lower[l])
        pass_list1.append(upper[u])
        pass_list1.append(digits[d])

    for i in range(g-3):
        i=random.randint(0,14)
        pass2.append(pass_list1[i])
    s=set(pass2)
    list(s)
    v=g-len((s))
    pass2=[]
    for i in s:
        pass2.append(i)
    for i in range(v):
        i = random.randint(0, 14)
        pass_list.append(pass_list1[i])
    random.shuffle(pass2)
    random.shuffle(pass_list)
    pass2.extend(pass_list)
    #print("".join(pass2),end="\n")
    s=[]
    for i in range(int(g/2)):
        random.shuffle(pass2[i:])
        s.append(pass2)
        password=''
    for i in pass2:
        password+=i
    return password
if __name__== "__main__":
    a=int(input("Enter the length of your password\n"))
    print(pass_gen(a))




