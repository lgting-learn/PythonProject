like_count = {}
with open("../testFile/students_like.txt", encoding="UTF-8") as fin:
    for line in fin:
        line = line[:-1]
        names, likes = line.split(" ")
        likes_list = likes.split(",")
        for like_item in likes_list:
            if like_item not in like_count:
                like_count[like_item] = 0
            like_count[like_item] += 1
print(like_count)
