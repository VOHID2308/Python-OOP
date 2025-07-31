class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def info(self):
        print(f"{self.name}, {self.age} yoshda, {self.grade} o‘quvchisi.")
student4 = Student("Sardor", 15, "9-sinf")
student4.info()