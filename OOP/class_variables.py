class Student:

    class_year = 2024
    num_students = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student('Desmond',19)
student2 = Student('Felicia', '20')
student3 = Student("frank", 52)


print(f'My graduating class of {Student.class_year} has {Student.num_students} students')