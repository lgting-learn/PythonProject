# root 当前目录
# dirs 当前目录下的子目录
# files 当前目录下的普通文件
import os

target_path = "/B站 100例题"
result = []
# 递归搜索目录
for root, dirs, files in os.walk(target_path):
    # if not os.path.isdir()
    for file in files:
        result.append((f"{root}/{file}", os.path.getsize(f"{root}/{file}")))
# 按大小降序排序，截取前三个文件
print(sorted(result, key=lambda x: x[1], reverse=True)[:3])
