class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I'm {self.name} and I'm {self.age} years old")    

class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Bark")