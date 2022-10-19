import  sqlite3
conn = sqlite3.connect("text.db")
cursor = conn.cursor()
cursor.execute("""create table if not exists goods(id int,
name text ,
num int,
price int,
weight int,
place text)""")
cursor.execute("""insert into goods (id,name,num,price,weight,place)
               select 234442,'牙刷',1234,12,23,'广东' union
               select 3242312,'茶叶',2344,100,40,'云南'
""")
cursor.execute("select id,name from goods where name = '牙刷'")
for row in cursor.fetchall():
    print(row)
conn.commit()
conn.close()



















