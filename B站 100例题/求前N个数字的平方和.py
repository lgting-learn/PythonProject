def get_square(num):
    result = 0
    for i in range(1, num + 1):
        result += i * i
    return result


print(get_square(3))
print(get_square(5))
print(get_square(10))
