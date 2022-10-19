# 1、局部变量和全局变量重名，就近原则
# 2、方法执行结束局部变量会被回收
num = 2


def autofunc():
    num = 1
    print(f"局部num---{num}")
    num += 1


for i in range(3):
    print(f"全局num {num}")
    num += 1
    autofunc()
