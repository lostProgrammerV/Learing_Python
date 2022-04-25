class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I'm {self.name} and I'm {self.age} years old")    

    def speak(self):
        print("Idk what I say")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

class Dog(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass        

d = Dog("Tim", 19)
d.show()
d.speak()

c = Cat("Bill", 34)
c.show()
c.speak()

f = Fish("Bublles", 10)
f.show()
f.speak()