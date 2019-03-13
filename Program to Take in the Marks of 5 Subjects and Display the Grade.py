sub1 = int(input("Enter the marks of the first subject: "))
sub2 = int(input("Enter the marks of the second subject: "))
sub3 = int(input("Enter the marks of the third subject: "))
sub4 = int(input("Enter the marks of the fourth subject: "))
sub5 = int(input("Enter the marks of the fifth subject: "))
sub6 = int(input("Enter the marks of the sixth subject: "))
sub7 = int(input("Enter the marks of the seventh subject: "))
sub8 = int(input("Enter the marks of the eighth subject: "))
sub9 = int(input("Enter the marks of the ninth subject: "))
sub10 = int(input("Enter the marks of the tenth subject: "))
avg = (sub1+sub2+sub3+sub4+sub5+sub6+sub7+sub8+sub9+sub10)/10
if(avg >=90):
    print("Grade: A")
    elif(avg>=80&avg<90):
        print("Grade: B")
        elif(avg >=70& avg<80):
            print("Grade: C")
            elif(avg >=60&avg<70):
                print("Grade: D")

                else:
                    print("Grade: F")
