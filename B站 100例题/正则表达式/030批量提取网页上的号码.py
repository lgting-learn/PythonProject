import re

pattern = r"1[3-9]\d{9}"

content = ""
with open("../testFile/029webpage_phone.txt",encoding="UTF-8") as fin:
    content = fin.read()

results = re.findall(pattern, content)

for result in results:
    print(result)
