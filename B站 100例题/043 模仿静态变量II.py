# 类和main方法中的变量重名时，变量各自独立
class Num:
    num = 1

    def inc(self):
        self.num += 1
        print(f"类里面的num---{self.num}")


if __name__ == '__main__':
    num = 200
    a = Num()
    for i in range(3):
        num += 1
        print(f"main里面的num {num}")
        a.inc()
