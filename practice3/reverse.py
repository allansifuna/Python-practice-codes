def reverse(b):
    a=b.split(" ")
    d=[]
    for i in a:
        i=i[::-1]
        d.append(i)
    print(" ".join(d))
    print("or\r")
    print(b[::-1])
reverse(input("Enter a short sentence\n"))