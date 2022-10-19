import datetime

curr_time = datetime.datetime.now()
print(curr_time, type(curr_time))
str_time = curr_time.strftime("%Y-%m-%d %H:%M:%S")
print(str_time)  # 2022/10-04 11:38:00

print(f"year {curr_time.year}")
print(f"month {curr_time.month}")
print(f"day {curr_time.day}")
print(f"hour {curr_time.hour}")
print(f"minute {curr_time.minute}")
print(f"second {curr_time.second}")
