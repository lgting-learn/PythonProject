import datetime

birth = "1995-08-28"
# 字符串变成对象
birth_day = datetime.datetime.strptime(birth, "%Y-%m-%d")
print(birth_day, type(birth_day))

curr_time = datetime.datetime.now()
print(curr_time, type(curr_time))

minus_time = curr_time - birth_day
print(minus_time, type(minus_time))
print(minus_time.days)
