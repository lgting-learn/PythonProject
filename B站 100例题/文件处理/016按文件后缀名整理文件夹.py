import os
import shutil

# 根据不同文件后缀，生成对应文件夹，且将文件归类

dir = "../arrange_dir"

for file in os.listdir(dir):
    # 截取后缀名
    ext = os.path.splitext(file)[1]
    # 截取.后面的后缀
    ext = ext[1:]
    if not os.path.isdir(f"{dir}/{ext}"):
        # 移动文件
        os.mkdir(f"{dir}/{ext}")
    source_path = f"{dir}/{file}"
    target_path = f"{dir}/{ext}/{file}"
    shutil.move(source_path, target_path)
