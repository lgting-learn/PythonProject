# Person继承Object
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"{self.name} {self.age}")


# Student继承Person
class Student(Person):
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)
        self.stu_no = stu_no

    # 子类想输出stu_no，父类info不满足，进行方法重写
    def info(self):
        super().info()
        print(f"子类的stu_no {self.stu_no}")


stu = Student("张三", 20, "111")
stu.info()
