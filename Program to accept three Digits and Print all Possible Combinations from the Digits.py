a = int(input("Enter the firt digit: "))
b = int(input("Enter the second digit: "))
c = int(input("Enter teh third digit: "))
d = []
d.append(a)
d.append(b)
d.append(c)
for i in range (0,3):
    for j in range (0,3):
        for  k in range(0,3):
            if (i!= j&j!=k&k!=i):
                print(d[i], d[j], d[k])


input("Press Enter to Exit!")
