import os
print(os.walk('./'))
for dirpath,dirnames,files in os.walk('./'):
    print('发现文件夹',dirpath)
    print(dirnames)#dirpath这个文件夹下的子文件夹列表
    print(files)#dirpath这个文件夹下的文件列表