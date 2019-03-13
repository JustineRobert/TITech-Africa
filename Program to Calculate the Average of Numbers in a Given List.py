n = int(input("Enter the number of elements to be inserted: "))
a =[]
for i in range(0,n):
    elem = int(input("Enter the element: "))
    a.append(elem)

avg = sum(a)/n

print("The average of the elements in the list", round(avg, 2))

input("Press Enter to Exit!")
    
