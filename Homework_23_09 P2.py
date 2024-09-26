
def move_last_to_first(my_list_1):
    if not my_list_1:
        return my_list_1
    return [my_list_1[-1]] + my_list_1[:-1]

my_list_1 = [12, 3, 4, 10]
new_list = move_last_to_first(my_list_1)
print(new_list)






