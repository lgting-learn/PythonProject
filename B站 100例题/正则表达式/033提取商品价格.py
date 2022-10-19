content = """
小明上街买菜
买了1斤黄瓜花了8元;
买了2斤葡萄花了13.5元;
买了3斤白菜花了5.4元
"""

# 要求提取(1、黄瓜、8)、(2、葡萄、13.5)、(3、白菜、5.4)


import re

"""正则：
.*在一起就表示任意字符出现零次或多次
? 前面可有可无
()对重量 物品 价格进行分组
"""
pattern = r"(\d+)斤(.*)花了(\d+(\.\d+)?)元"
# for line in content.split("\n"):
#     results = re.search(pattern, line)
#     if results:
#         print(f"{results.group(1)}\t{results.group(2)}\t{results.group(3)}")

results = re.findall(pattern, content)
print(results)
# result是元组 没有group()方法
for result in results:
    print(f"{result[0]}\t{result[1]}\t{result[2]}")
