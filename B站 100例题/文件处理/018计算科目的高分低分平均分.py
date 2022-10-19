# 字典{key,value}
course_grade = {}
with open("../testFile/course_student_grade_input.txt", encoding="UTF-8") as fin:
    for line in fin:
        line = line[:-1]
        course, sno, name, grade = line.split(",")
        if course not in course_grade:
            course_grade[course] = []
        course_grade[course].append(int(grade))

for course, grade in course_grade.items():
    print(course,
          max(grade),
          min(grade),
          sum(grade) / len(grade)
          )
