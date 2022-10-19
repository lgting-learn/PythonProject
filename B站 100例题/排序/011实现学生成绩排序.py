# 复杂列表；元素是字典或元组
# [{'sno':101,'name':xx}]
stus = [
    {'sno':101,'name':'001'},
    {'sno':104,'name':'004'},
    {'sno':102,'name':'002'},
    {'sno':103,'name':'003'},
]
# sno升序排序
# 入参x：每个元素
# x['sno']：元素的对应字段值
stus_sorta = sorted(stus,key=lambda x:x['sno'])
# sno降序
stus_sortb = sorted(stus,key=lambda x:x['sno'],reverse=True)
print(stus)
print(stus_sorta)
print(stus_sortb)