import datetime

is_first_line = True
date_sale_list = {}
with open("../testFile/027sale_date.txt", encoding="UTF-8") as fin:
    for line in fin:
        if is_first_line:
            is_first_line = False
            continue
        line = line[:-1]
        date_data, sale_data = line.split(" ")
        date_sale_list[date_data] = float(sale_data)


# 获取日期七天的日期
def get_date_week(pdate, days):
    # 字符串转时间对象
    pdate_obj = datetime.datetime.strptime(pdate, "%Y-%m-%d")
    day7_delta = datetime.timedelta(days=days)
    week_date = (pdate_obj - day7_delta).strftime("%Y-%m-%d")
    return week_date


for date_data, sale_data in date_sale_list.items():
    week_date = get_date_week(date_data, 7)
    week_date_sale = date_sale_list.get(week_date, 0)
    if week_date_sale == 0:
        print(date_data, sale_data, 0)
    else:
        finally_rate = round((sale_data - week_date_sale) / week_date_sale, 2)
        print(date_data, sale_data, week_date, week_date_sale, finally_rate)
