class Student:
    def __init__(self, name,age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_avarage_grade(self):
        pass

s1 = Student("TIm", 19, 99)
s2 = Student("Bill", 19,67)
s1 = Student("Tomy", 19, 34)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
