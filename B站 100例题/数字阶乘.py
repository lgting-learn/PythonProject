def jiecheng(number):
    while number == 1:
        return 1
    return number * jiecheng(number - 1);
print(jiecheng(6))
