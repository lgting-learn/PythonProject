import datetime

unix_time = 1620747647
datetime_obj = datetime.datetime.fromtimestamp(unix_time)
# 字符串格式成时间
datetime_str = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
print(datetime_str)
