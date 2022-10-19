def get_unique_list(lista):
    arr=[]
    for i in lista:
        if i not in arr:
            arr.append(i)
    return arr
lista=[1,2,1,2,1,5]
print(get_unique_list(lista))
# 转成列表
print(list(set(lista)))