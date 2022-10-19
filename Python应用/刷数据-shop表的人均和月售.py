import pymysql
import random

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='115336', db='elemensys')
cursor = conn.cursor()

sqlstr = 'select * from shop'
cursor.execute(sqlstr)
data = cursor.fetchall()
for item in data:
    id = item[0]  # 获取店铺id
    category = random.randint(0, 15)  # 随机0到15，对应首页16种食品类别
    month_sales = random.randint(20, 2000)  # 月售
    per_capita = random.randint(15, 50)  # 人均
    sqlstr = "update shop set category='{}',per_capita='{}',month_sales='{}' where id='{}'".format(category,
                                                                                                        per_capita,
                                                                                                        month_sales, id)
    cursor.execute(sqlstr)

print('shop表的分类,人均,月售数据刷新完毕')
conn.commit()
cursor.close()
conn.close()
