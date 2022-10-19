def get_all_even(start, end):
    list = []
    for i in range(start, end):
        if i % 2 == 0:
            list.append(i)
    print(f"偶数列表{list}")
get_all_even(4,15)