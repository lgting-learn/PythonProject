def add(a, b):
    return a + b


if __name__ == '__main__':
    print(add(1, 2))  # 运行当前模块才打印，其他模块调用本模块不会打印
