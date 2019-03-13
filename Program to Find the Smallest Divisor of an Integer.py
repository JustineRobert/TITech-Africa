n = int(input("Enter an Integer: "))
m =[]
for i in range(2, n+1):
    if(n%i==0):
        m.append(i)
        m.sort()

        print("Smallest Divisor is: ", m[0])


input("Press Enter to Exit!")
