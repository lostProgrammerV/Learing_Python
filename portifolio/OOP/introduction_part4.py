class Person:
    number_of_people = 0

    def __init__(self,name):
        self.name = name

p1 = Person("Aler")
p2 = Person("Jill")

Person.number_of_people = 8

print(p2.number_of_people)
