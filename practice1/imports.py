import random
for z in range(10):
    for i in range(4):
        for j in range(4):
            for t in range(4):
                print("%d" % (random.randint(1, 9)), end="")
            print("", end=" ")
        print("\t")
    print("\n")