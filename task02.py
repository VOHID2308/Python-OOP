class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

student1 = Student("Ali", 15, "9-sinf")
student2 = Student("Laylo", 14, "8-sinf")
student3 = Student("Javlon", 16, "10-sinf")
print(student1.name, student1.age, student1.grade)
