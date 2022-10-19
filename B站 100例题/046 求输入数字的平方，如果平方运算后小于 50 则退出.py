def SQ(x):
    return x * x


flag = True
while flag:
    num = int(input("请输入："))
    if SQ(num) < 50:
        flag = False
        print(f"计算结果{SQ(num)}小于50退出")
    else:
        print(f"计算结果为：{SQ(num)}")

