class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def changeAge(self, age):
        self.age = age

    def __str__(self):
        return self.name + "--" + str(self.age)

#-----------------------------------------------

class Addr:

    def __init__(self, city, state):
        self.city = city
        self.state = state

    def changeCity(self, city):
        self.city = city

    def __str__(self):
        return self.city + "--" + self.state

#-----------------------------------------------

class Student(Person, Addr):

    def __init__(self, name, age, city, state, grade, gpa):
        Person.__init__(self, name, age)
        Addr.__init__(self, city, state)
        self.grade = grade
        self.gpa = gpa

    def changeGpa(self, gpa):
        self.gpa = gpa

    def changeAge(self, age):
        self.age = age + 23

    def __str__(self):
        return Person.__str__(self) + "--" + Addr.__str__(self) + "--" +str(self.grade) + "--" + str(self.gpa)

#------------------------------------------------
    
s1 = Student("John", 18, "New York", "NY", 12, 3.8)
print(s1)

s2 = Student("Mahmut", 46, "İstanbul", "Kadıköy", 17, 4.5)
print(s2)

s1.changeAge(67)
print(s1)

s1.changeCity("Sivas")
print(s1)

s2.changeAge(25)
print(s2)


