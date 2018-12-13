def ishashad(a):
    d=0
    count=0
    for i in str(a):
        d+=int(i,10);
        count+=1
    if a%d==0 and count!=1:
        print("True")
    else:
        print("False")
c=int(input("Enter a number to check\n"))
ishashad(c)