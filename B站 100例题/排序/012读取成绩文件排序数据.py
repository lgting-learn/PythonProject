# with语句的目的是简化try/finally模式，用于保证一段代码运行完毕之后能够执行某项操作，
# 即便代码由于**异常、return语句或者sys.exit()**调用而中止
# try:
#     f = open('test.txt')
#     f.read()
# finally:
#     f.close()


def read_file():
    result = []
    with open("../testFile/student_grade_input.txt") as file:
        for line in file:
            # 除了最后一个\n不截取
            line = line[:-1]
            result.append(line.split(","))
        return result


def sort_grade(datas):
    return sorted(datas, key=lambda x: int(x[2]), reverse=True)


def write_file(datas):
    with open("../testFile/student_grade_output.txt", "w") as file:
        for line in datas:
            file.write(",".join(line)+"\n")

# 读取文件
datas = read_file()
# 按成绩降序排序数据
datas = sort_grade(datas)
# 写入文件
write_file(datas)
