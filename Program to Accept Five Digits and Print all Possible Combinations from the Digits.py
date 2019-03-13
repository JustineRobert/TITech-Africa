a = int(input("Enter first digit: "))
b = int(input("Enter second digit: "))
c = int(input("Enter the third digit: "))
d = int(input("Enter the fourth digit: "))
e = int(input("Enter the fifth digit: "))
f = []

f.append(a)
f.append(b)
f.append(c)
f.append(d)
f.append(e)

for i in range(0, 5):
    for j in range(0, 5):
        for k in range(0, 5):
            for l in range(0, 5):
                for m in range(0, 5):
                    if(i!=j&j!=k&k!=l&l!=m&m!=i):

                        print(f[i], f[j], f[k], f[l], f[m])

input("Press Enter to Exit!")
