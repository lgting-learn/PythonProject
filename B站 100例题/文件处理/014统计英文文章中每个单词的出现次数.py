word_count = {}
with open("../testFile/014.txt") as fin:
    for line in fin:
        line = line[:-1]
        words = line.split()
        for word in words:
            if word not in word_count:
                word_count[word] = 0
            word_count[word] += 1
# 按出现次数降序排序 只看前两个
word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:2]
print(word_count)
