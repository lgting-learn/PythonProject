import re

content = """
白日依山323232尽，黄河入18376004506海流18376004507
"""
# " r "代表了原生字符串
pattern = r"1[3-9]\d{9}"
results = re.findall(pattern, content)
for result in results:
    print(result)
