# Inheritance
class person:
    def __init__(self, name, age, gender): #Function
        self.name = name
        self.age = age
        self.gender = gender
        print("Name is {}, age is {} and gender is {}".format(self.name, self.age, self.gender))


class teacher(person):
    def print(self, name, age, gender):
        person.__init__(self, name, gender) #calling the function

class student(person):
    def print(self, name, age, gender):
        person.__init__(self, name, age, gender) # Calling the function
