def exchange(x, y):
    x, y = y, x
    return x, y


a = 1
b = 2
print(a, b)
a, b = exchange(a, b)
print(a, b)
