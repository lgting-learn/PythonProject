# 方法一：按行读取
# for line in fin
#     方法二：一次读取所有内容到一个字符串
# content = fin.read()

import os

dir = "../testFile"

content = ''
for file in os.listdir(dir):
    file_path = f"{dir}/{file}"
    # 文件 + txt结尾
    if os.path.isfile(file_path) and file_path.endswith("txt") and file_path.find("多个") == -1:
        with open(f"{file_path}", encoding="UTF-8") as fin:
            content += ("文件：" + file + "\n" + fin.read())
print("content" + content)
with open("../testFile/多个文件合并.txt", "w", encoding="UTF-8") as fout:
    fout.write(content)
