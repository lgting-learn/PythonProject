"""
写一个函数，验证密码是否满足条件
1、长度位于[6,20]之间
2、必须包含至少1个小写字母
3、必须包含至少1个大写字母
4、必须包含至少1个数字
5、必须包含至少1个特殊字符
返回 True,None
或者 False,原因
"""

import re

"""
r 表示原生字符串（rawstring），该字符串声明了引号中的内容表示该内容的原始含义，避免了多次转义造成的反斜杠困扰。
re.match("d:\\\\")
re.match(r"d:\\")
"""


def check_pwd(pwd):
    if not 6 <= len(pwd) <= 20:
        return False, "长度位于[6,20]之间"
    if not re.findall(r"[a-z]", pwd):
        return False, "必须包含至少1个小写字母"
    if not re.findall(r"[A-Z]", pwd):
        return False, "必须包含至少1个大写字母"
    if not re.findall(r"[0-9]", pwd):
        return False, "必须包含至少1个数字"
    if not re.findall(r"[^a-zA-Z0-9]", pwd):
        return False, "必须包含至少1个特殊字符"
    return True, None


print("Helloworld#666", check_pwd("Helloworld#666"))
print("Helloworld#", check_pwd("Helloworld#"))
print("helloworld#666", check_pwd("helloworld#666"))
print("Helloworld666", check_pwd("Helloworld666"))
