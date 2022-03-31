from webbrowser import get


class Dog: #definition

    def __init__(self, name, age):
       self.name = name
       self.age = age

    def add_one(self, x):
        return x + 1

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    def bark(self): # type
        print("bark")
         
d = Dog("Tim", 7) #news instances right now
print(d.get_name(), d.get_age())

d2 = Dog("Bill", 12)
print(d2.get_name(), d2.get_age())

d.bark() #cast the dog class

print(d.add_one(5))

print(type(d))


    