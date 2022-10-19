# 简单列表：元素类型不是复合类型的（列表/元组/字典）
# 知识点：
# 1、怎样原地排序？怎样不改变原列表排序
# 2、怎样指定是升序还是降序排序
lista = [2, 4, 3, 5, 1]
# 改变原数组
# lista.sort()
# 降序排序
# lista.sort(reverse=True)

# 不改变原数组lista
# listb = sorted(lista)
# 降序排序
listb = sorted(lista, reverse=True)

print(f"lista is {lista}")
print(f"listb is {listb}")
