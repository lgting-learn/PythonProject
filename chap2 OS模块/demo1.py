import os
lst = os.listdir('../chap1')
for item in lst:
    print(item,type(item))

lstScan = os.scandir('../chap1')
for item in lstScan:
    print(item,type(item),item.name, item.path,item.is_dir())
