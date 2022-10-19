count = 1

while count <= 7:
    num = int(input("请输入："))
    while num < 1 or num > 50:
        num = int(input("请输入1-50之间的整数："))
    print(num * "*")
    count += 1
