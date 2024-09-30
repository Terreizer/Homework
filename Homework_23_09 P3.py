def split_list(input_list):
    if len(input_list) == 0:
        return [[], []]
    mid = (len(input_list) + 1) // 2
    list_1 = input_list[:mid]
    list_2 = input_list[mid:]
    return [list_1, list_2]
print(split_list([]))
print(split_list([1, 2, 3, 4, 5, 6]))
print(split_list([1, 2, 3]))
print(split_list([1, 2, 3, 4, 5]))
print(split_list([1]))
