def fun():
    for i in range(20):
        yield i
gen=fun()
print(next(gen))
