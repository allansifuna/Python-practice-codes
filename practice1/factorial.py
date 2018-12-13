def factorial(a):
    d=1
    for i in range(1,a+1):
        d*=i
    return d
def count(s):
    s=str(s)
    d=[]
    for i in s:
        d.append(i)
    for i,d in enumerate(d):
        print(i,d)
b=int(input("Enter a number to get factorials\n"))
c=factorial(b)
count(c)