lower = int(input("Enter the lower limit number for the range: "))
upper = int(input("Enter the upper limit number for the range: "))
for i in range (lower, upper+1):
    if (i%2!=0):
        print(i)


input("Press Enter to Exit!")
