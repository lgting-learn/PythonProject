course_teacher_map = {}
# 将文件数据以字典形式保存
with open("../testFile/course_teacher.txt", encoding='UTF-8') as fin:
    for line in fin:
        line = line[:-1]
        course, teacher = line.split(",")
        course_teacher_map[course] = teacher

content = ''
with open("../testFile/course_student_grade_input.txt", encoding="UTF-8") as fin:
    for line in fin:
        line = line[:-1]
        course, sno, name, grade = line.split(",")
        temp_content = f"{course},{course_teacher_map[course]},{sno},{name},{grade}\n"
        content += temp_content

with open("../testFile/course_teacher_out.txt", "w", encoding="UTF-8") as fout:
    fout.write(content)
