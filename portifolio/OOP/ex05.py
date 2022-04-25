class Person:
    number_of_people = 0
    gravity = -9.8

    def __init__(self,name):
        self.name = name
        Person.add_person()

    @classmethod    
    def number_of_people(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1    

p1 = Person("Aler")
p2 = Person("Jill")

#Person.number_of_people = 8

p1 = Person("Tim")
print(Person.number_of_people)
P2 = Person("Jill")
print(Person.number_of_people)
print(Person.number_of_people())