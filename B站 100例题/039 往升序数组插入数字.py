"""
题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。
"""

# 0 作为加入数字的占位符
a = [1, 4, 6, 9, 13, 16, 19, 28, 40, 100, 0]
# 将比target大的数往后挪一位
target = int(input("请输入数字："))
local = 0
# -1表示倒序输出
for i in range(len(a) - 2, -1, -1):
    if a[i] > target:
        local += 1
local = len(a) - 1 - local

for i in range(len(a) - 1, local - 1, -1):
    a[i] = a[i - 1]

a[local] = target

print(a)
