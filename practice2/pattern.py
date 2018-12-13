def inp(r):
    print(r)
    r = r.lstrip(" ").rstrip(" ")
    a, b = r.split(' ')
    d = []
    d.append(int(a, 10))
    d.append(int(b, 10))
    return d


if __name__ == "__main__":
    def hor(x):
        for i in range(x):
            print("+  ", end="")
            for j in range(4):
                print("-  ", end="")
        print("+\n", end="")

    def ver(y):
        for i in range(4):
            for j in range(y + 1):
                print("|" + " " * 14, end="")
            print("\r")

    a = input("Enter the number of rows and columns\n")
    d = inp(a)
    c = d[1]
    r = d[0]
    if c != 0 and r != 0:
        if r < c:
            s = c
        elif c < r:
            s = c
        else:
            s = c
        if r < 0:
            print("Enter a value greater than or equal to 1\n")
        else:
            for i in range(r):
                hor(s)
                ver(s)
            hor(c)
    pass
else:
    pass
