import os

sum_size = 0
for file in os.listdir(".."):
    # 判断是否为文件，排除文件夹
    if os.path.isfile(file):
        # 子节
        sum_size += os.path.getsize(file)
        print(file, os.path.getsize(file))
print(round(sum_size / 1024, 2))
