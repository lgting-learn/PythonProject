class test:
    x = 0
    c = 0


def f(stu):
    stu.x = 20
    stu.c = 'c'


a = test()
a.x = 3
a.c = 'a'
f(a)
print(a.x, a.c)
