import re

content = """
白日依山323232尽，黄河入18376004506海流15376004507
"""
# 加了一个分组
pattern = r"(1[3-9])\d{9}"
# \1 匹配第一个分组 \n引用第n个分组
print(re.sub(pattern, r"\1******", content))
