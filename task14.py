class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"{self.name}, {self.age} years old")

def main():
    student1 = Student("Malika", 20)
    student2 = Student("Ali", 25)
    student3 = Student("Diyorbek", 20)
    student4 = Student("farangiz", 16)
    student5 = Student("Dilshoda", 9)

    max([student1, student2, student3, student4, student5], key=lambda i: i.age).show_info()

if __name__ == "__main__":
    main()