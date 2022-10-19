import re


def date_is_right(date):
    return re.match("\d{4}-\d{2}-\d{2}", date) is not None


date1 = "2022-10-04"
date2 = "202-10-04"
date3 = "2022/10-04"
date4 = "20221004"

print(date1, date_is_right(date1))
print(date2, date_is_right(date2))
print(date3, date_is_right(date3))
print(date4, date_is_right(date4))
