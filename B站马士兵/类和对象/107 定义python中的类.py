# Student 类对象
class Student:
    # 直接写在类内部且不在方法中的变量称为类属性，使用类名直接访问，被所有对象共享
    come_from = "广东"

    # 初始化方法
    def __init__(self, name, age):
        # self.name 称为实例属性，局部变量name赋值给self.name
        # 实例属性被所有对象共享
        self.name = name
        self.age = age

    # 实例方法
    def eat(self):
        print("学生吃饭")

    # 静态方法，参数没有self；使用类名直接访问
    @staticmethod
    def method():
        print("staticmethod修饰的是静态方法")

    # 类方法；使用类名直接访问,cls不需要传入
    @classmethod
    def cm(cls):
        print("classmethod修饰的是类方法")


# 定义在类之外的叫函数，在类内部定义的叫方法
def drink():
    print("喝水函数")


# 实例对象中有类指针指向类
stu = Student("小米", 20)  # 调用init
stu.eat()  # 对象.方法()
Student.eat(stu)  # 类.方法(类的对象) self参数指向自身，所以可以传入类的对象

Student.cm()  # 类方法
Student.method()  # 静态方法

# 动态绑定属性和方法
stu.gender = "女"
print(stu.gender)

stu.drink = drink
stu.drink()
