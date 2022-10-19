import datetime


def get_date_range(begin_date, end_date):
    date_list = []
    while begin_date <= end_date:
        date_list.append(begin_date)
        # strftime：
        # f表示format，表示格式化，和strptime正好相反，要求给一个时间对象和输出格式，返回一个时间字符串。
        # strptime：
        # p表示parse，表示分析的意思，所以strptime是给定一个时间字符串和分析模式，返回一个时间对象
        begin_date_obj = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
        print(f"strptime {begin_date_obj},{type(begin_date_obj)}")
        day1_delta = datetime.timedelta(days=1)
        begin_date = (begin_date_obj + day1_delta).strftime("%Y-%m-%d")
        print(f"strftime {begin_date},{type(begin_date)}")

    return date_list


print(get_date_range("2021-04-28", "2021-05-03"))
