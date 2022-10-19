import re

with open("../testFile/036 english article.txt") as fin:
    content = fin.read()

# 只能指定单个字符进行分割
# print(content.split())
# 指定多个字符分割
words = re.split(r"[\s.()-?\"\\'\\]+",content)

# 计算每个单词出现次数
import pandas as pd
print(pd.Series(words).value_counts()[:20])
