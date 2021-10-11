def addition():
    print("Addition")
    n = float(input("Enter the number: "))
    t = 0 #Total number enter
    ans = 0
    while n != 0:
        ans = ans + n
        t+=1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans,t]

def subtraction ():
    print("Subtraction");
    n = float(input("Enter the number: "))
    t = 0 #Total number enter
    sum = 0
    while n != 0:
        ans = ans - n
        t+=1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans,t]

def multiplication ():
    print("Multiplication")
    n = float(input("Enter the number: "))
    t = 0 #Total number enter
    ans = 1
    while n != 0:
        ans = ans * n
        t+=1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans,t]

def average():
    an = []
    an = addition()
    t = an[1]
    a = an[0]
    ans = a / t
    return [ans,t]

#def squareit(n):
    # squaredlist = []
    # res = n**2
    # squaredlist.append(res)
    # return squaredlist[0]

while True:
    list = []
    print(" My first python program!")
    print(" Simple Calculator in python by Malik Umer Farooq")
    print(" Enter 'a' for addition")
    print(" Enter 's' for substraction")
    print(" Enter 'm' for multiplication")
    print(" Enter 'v' for average")
    #print(" Enter 'sqr' for square of a number")
    print(" Enter 'q' for quit")
    c = input(" ")
    if c != 'q':
        if c == 'a':
            list = addition()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == 's':
            list = subtraction()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == 'm':
            list = multiplication()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == 'v':
            list = average()
            print("Ans = ", list[0], " total inputs ",list[1])
        # elif c == 'sqr':
        #     n = float(input(enter a number you wish to square))
        #     list = squareit()
        #     print("Ans = ", list[0], " total inputs ",list[n])
        else:
            print ("Sorry, invilid character")
    else:
        break
