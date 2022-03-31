class Dog: #definition

    def __init__(self, name):
       self.name = name
       print(name)

    def add_one(self, x):
        return x + 1

    def bark(self): # type
        print("bark")
         
d = Dog("Tim") #news instances right now
d.bark() #cast the dog class

print(d.add_one(5))

print(type(d))


    