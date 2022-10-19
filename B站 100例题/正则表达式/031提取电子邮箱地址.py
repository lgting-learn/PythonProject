content = """
222@qq.com
朝代：元
东西222#qq.com 221@qq.com
"""

import re

"""
re.VERBOSE 在正则表达式字符串中允许空白字符和注释,让它更可读（允许换行）
+ 最少出现一次
\. 转译
{2,4} [2,4]
"""
pattern = re.compile(
    """
    [a-zA-Z0-9_-]+
    @
    [a-zA-Z0-9]+
    \.
    [a-zA-Z]{2,4}
    """, re.VERBOSE
)

results = re.findall(pattern, content)
for result in results:
    print(result)
