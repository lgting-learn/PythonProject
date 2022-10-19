import os
import json

stu_info_path = "./student_self.txt"
file_not_exist_tip = "暂未保存学生信息"
input_error_tip = "输入有误"


# 菜单
def menu():
    print("==========================学生信息管理系统==========================")
    print("------------------------------功能菜单-----------------------------")
    print('\t\t\t   1.录入学生信息')
    print('\t\t\t   2.查找学生信息')
    print('\t\t\t   3.删除学生信息')
    print('\t\t\t   4.修改学生信息')
    print('\t\t\t   5.排序')
    print('\t\t\t   6.统计学生总人数')
    print('\t\t\t   7.显示所有学生信息')
    print('\t\t\t   0.退出系统')
    print('-------------------------------------------------------------------')


# def exit():
#     input_user = input()
#     print(input_user)
#     if "exit" == input_user:
#         return


def main():
    menu()
    exceptFlag = False
    while True:
        try:
            choise = int(input("请重新选择：")) if exceptFlag else int(input("请选择："))
        except:  # try抛出异常
            exceptFlag = True
            print("您的输入有误，请输入功能菜单存在的序列数")
        else:  # 用户正确输入
            if choise == 0:  # 退出系统
                answer = input("您确定要退出系统吗？y/n\n")
                if answer.lower() == "y":
                    break
                elif answer.lower() == "n":
                    continue
            elif choise == 1:  # 录入学生信息
                insert()
            elif choise == 2:  # 查找学生信息
                search()
            elif choise == 3:  # 删除学生信息
                delete()
            elif choise == 4:  # 修改学生信息
                modify()
            elif choise == 5:  # 排序
                sort()
            elif choise == 6:  # 统计学生总人数
                total()
            elif choise == 7:  # 显示所有学生信息
                show()


def sort():
    show()
    # False 升序 True降序
    reverse_flag = False
    input_sort = int(input("请选择（0.升序 1.降序:）"))
    inpt_sort_type = input("请选择排序方式（1.按英语成绩排序 2.按python成绩排序 3.按java成绩排序 0.按总成绩排序）：")
    sort_type_dict = {
        "1":"english",
        "2":"python",
        "3":"java",
        "0":"all_grade"
    }
    student_old = get_student_list()
    for item in student_old:
        item["all_grade"] = int(item.get('english')) + int(item.get('python')) + int(item.get('java'))
        if 1 == input_sort:
            reverse_flag = True
    stu_sort = sorted(student_old, key=lambda x: x[sort_type_dict[inpt_sort_type]], reverse=reverse_flag)
    show_student(stu_sort)


# 获取全部学生信息
def get_student_list():
    student_old = []
    with open(stu_info_path, encoding="utf-8") as fin:
        for line in fin:
            # 字符串转为字典
            line = eval(line)
            student_old.append(line)
        return student_old


def delete():
    if os.path.exists(stu_info_path):
        show()
        while True:
            input_id = input("请输入要删除的学生的ID：")
            student_old = get_student_list()

            if student_old:
                for line in student_old:
                    if str(input_id) == str(line["id"]):
                        student_old.remove(line)
                print(f"ID为{input_id}的学生信息已被删除\n")
                save(student_old, "delete")
                show()
                choise = input("是否继续删除？y/n\n")
                if choise.lower() == 'y':
                    continue
                elif choise.lower() == 'n':
                    break
            else:
                print(f"删除失败，不存在ID为{input_id}的学生")
    else:
        print(file_not_exist_tip)


def modify():
    if os.path.exists(stu_info_path):
        show()
        student_old = get_student_list()

        input_list = {
            "name": "请输入名字：",
            "english": "请输入英语成绩：",
            "python": "请输入python成绩：",
            "java": "请输入java成绩："
        }
        while True:
            answer = input("请输入要修改的学员的ID：")

            with open(stu_info_path, "w", encoding="utf-8") as fout:
                for line in student_old:
                    if str(answer) == str(line['id']):
                        print("找到学生信息，可以修改他的相关信息了！")
                        for key, value in input_list.items():
                            line[key] = input(value)
                    fout.write(str(line) + "\n")

            choise = input("是否继续修改其他学生信息呢？y/n\n")
            if choise.lower() == 'y':
                continue
            elif choise.lower() == 'n':
                print("修改后的学生信息如下：\n")
                show()
                break
            else:
                print(input_error_tip)
    else:
        print(file_not_exist_tip)


# 显示所有学生信息
def show():
    if os.path.exists(stu_info_path):
        line_query_list = []
        with open(stu_info_path, encoding="utf-8") as fin:
            for line in fin:
                line_query_list.append(eval(line))
            show_student(line_query_list)
    else:
        print(file_not_exist_tip)


# 录入学生信息
def insert():
    input_list = {
        "id": "ID(如1001)",
        "name": "名字",
        "english": "英语成绩",
        "python": "python成绩",
        "java": "java成绩"
    }
    stus_list = []
    input_list_file = {}
    while True:
        for type, tip in input_list.items():
            input_value = input(f"请输入{tip}：")
            input_list_file[type] = input_value
        stus_list.append(str(input_list_file))
        answer = input("是否继续添加？y/n\n")
        if answer == "y":
            continue
        elif answer == "n":

            break
    save(stus_list, "insert")
    print("学生信息录入完毕！")

# 统计总人数
def total():
    if os.path.exists(stu_info_path):
        with open(stu_info_path, encoding="utf-8") as fin:
            students = fin.readlines();
            if students:
                print(f"共有{len(students)}名学生")
            else:
                print("还未录入学生信息")
    else:
        print(file_not_exist_tip)


# 格式化输出学生信息
def show_student(line_query_list):
    # 如果字典有值
    if len(line_query_list) != 0:
        format_title = "{:^4}{:^12}{:^12}{:^12}{:^12}{:^12}"
        print(format_title.format("ID", "姓名", "英语成绩", "python成绩", "java成绩", "总成绩"))
        format_grade = "{:^4}{:^12}{:^14}{:^15}{:^12}{:^14}"
        for item in line_query_list:
            all_grade = int(item.get('english')) + int(item.get('python')) + int(item.get('java'))
            print(format_grade.format(
                item.get('id'),
                item.get('name'),
                item.get('english'),
                item.get('python'),
                item.get('java'),
                all_grade
            ))

    else:
        print("没有查询到学生信息，无数据显示")


# 格式化输出
def search():
    id = ''
    name = ''
    line_query = {}
    line_query_list = []
    while True:
        try:
            choise = int(input("按ID查找请输入1，按姓名查找请输入2："))
            if os.path.exists(stu_info_path):
                if choise == 1:
                    id = int(input("请输入要查询的学生ID："))
                elif choise == 2:
                    name = input("请输入学生姓名：")
                else:
                    print("您的输入有误")
                    continue
                with open(stu_info_path, encoding="utf-8") as fin:
                    for line in fin:
                        # eval可以把list,tuple,dict和string相互转化。
                        line = eval(line)
                        if id != '' and str(line['id']) == str(id):
                            line_query = line
                        elif name != '' and str(line['name']) == str(name):
                            line_query = line
                line_query_list.append(line_query)
                show_student(line_query_list)
            else:
                print(file_not_exist_tip)
                return


        except:
            print("您的输入有误，请输入1或2")


# 更新成绩文件
def save(stus_list, type):
    content = ''

    # 删除操作
    if "delete" == type:
        operation = "w"
    else:
        if os.path.exists(stu_info_path):
            operation = "a"
        else:
            operation = "w"

    stu_txt = open(stu_info_path, operation, encoding="utf-8")

    for line in stus_list:
        content += (str(line) + "\n")
    stu_txt.write(content)


if __name__ == '__main__':
    main()
