class Student:
    def __init__(self, age):
        # 私有属性
        self.__age = age

stu = Student(20)
# 访问报错
# print(stu.__age)
# 打印类的所有属性名和方法
# print(dir(stu))
print(f"输出私有变量__age：{stu._Student__age}")
