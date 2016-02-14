class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def changeAge(self, age):
        self.age = age

    def __str__(self):
        return self.name + "--" + str(self.age)

#-----------------------------------------------

class Student(Person):

    def __init__(self, name, age, grade, gpa):
        Person.__init__(self, name, age)
        self.grade = grade
        self.gpa = gpa

    def changeGpa(self, gpa):
        self.gpa = gpa

    def __str__(self):
        return Person.__str__(self) + "--" + str(self.grade) + "--" + str(self.gpa)

s1 = Student("john", 19, 18, 3.8)
print(s1)

s1.changeGpa(3.9)
print(s1)

s1.changeAge(25)
print(s1)
