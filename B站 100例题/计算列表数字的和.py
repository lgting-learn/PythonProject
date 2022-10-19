def get_list_add(list):
    result = 0
    for i in list:
        result += i
    return result


list = [1, 2, 3, 4]
print(f"{list}和为{get_list_add(list)}")
