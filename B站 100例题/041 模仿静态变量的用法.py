def varfun():
    var = 0
    print(var)
    var += 1


# 方法执行结束局部变量会被回收
varfun()  # 0
varfun()  # 0
varfun()  # 0


class Static:
    staticVar = 0

    def varfunc(self):
        self.staticVar += 1
        print(self.staticVar)


a = Static()
for i in range(3):
    # 依次打印123
    a.varfunc()
