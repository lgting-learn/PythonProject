class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"str()被重写：{self.name} {self.age}"

stu = Student("张三",22)
print(stu)
