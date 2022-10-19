import csv


def get_csv_data(csv_file, line):
    test_csv = open(csv_file, 'r', encoding='utf-8-sig')
    reader = csv.reader(test_csv)
    for index, row in enumerate(reader, start=1):  # 参数2 :决定了下标位置的开始计数方式
        if index == line:
            return row


if __name__ == "__main__":
    get_csv_data('./choose.csv', 1)
    get_csv_data('./choose.csv', 2)
    get_csv_data('./choose.csv', 3)
