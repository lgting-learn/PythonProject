import datetime
def get_diff_days(pdate,days):
    # 日期字符串转成对象
    pdate_obj = datetime.datetime.strptime(pdate,"%Y-%m-%d")
    time_gap = datetime.timedelta(days=days)
    print(time_gap,type(time_gap))
    pdate_result = pdate_obj-time_gap
    return pdate_result.strftime("%Y-%m-%d")

print(get_diff_days("1997-01-24",1))
print(get_diff_days("1997-01-24",30))