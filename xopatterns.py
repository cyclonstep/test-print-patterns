# print alternate x o beginning with x
def printX(n):
    # print("masuk sini X")
    for x in range(1, n):
        # print(f"x: {x}")
        if (x % 2 != 0):
            print("x")
        else:
            print("o")


# print alternate x o beginning with o
def printO(n):
    # print("masuk sini O")
    for x in range(1, n):
        # print(f"x: {x}")
        if (x % 2 != 0):
            print("o")
        else:
            print("x")

def printPatterns(n):
    # upper half n-1 lines for odd, n-2 lines for even
    x = n

    if (n % 2 == 0):
        x -= 1
    # number of spaces to leave in each line
    p = n - 1

    # number of characters in each line
    s = 1

    # something odd...
    # the // can be used for making division results are integers
    t = (x-1)//2

    print(f"t: {t}")

    for i in (range(1, t)):
        for j in range(1, p):
            print("-", end="")
        # print(f"s: {s}")
        if (i % 2 != 0):
            printX(s)
        else:
            printO(s)
        print("\n")
        p += 1

        for j in range(1, p):
            print("-", end="")
        
        if (i % 2 != 0):
            printX(s)
        else:
            printO(s)
        
        print("\n")
        
        p -= 1
        s += 1
    
    # extra upper middle for even
    if (n % 2 == 0):
        for i in range(1, p):
            print("-")
        
        if (n % 4 != 0):
            printX(n//2)
        else:
            printO(n//2)
        
        print("\n")
    
    # middle line
    if (n % 2 != 0):
        printX(n)
    else:
        if (n % 4 != 0):
            printX(n//2)
            printX(n//2)
        else:
            printX(n//2)
            printO(n//2)
    
    print("\n")
    
    # extra lower middle for even
    if (n % 2 == 0):
        print(" ")
        printX(n//2)
        print("\n")

    # lower half
    p = 1
    
    if (n % 2 == 0):
        x -= 1
        p = 2
    
    q = x // 2


    
        

if __name__ == '__main__':
    printPatterns(5)