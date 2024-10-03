def move_zeros(lst):
    pos = 0
    for i in range(len(lst)):
        if lst[i] != 0:
            lst[pos], lst[i] = lst[i], lst[pos]
            pos += 1

my_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
move_zeros(my_list)
print(my_list)