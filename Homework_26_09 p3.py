import random

random_list = random.sample(range(1, 100), random.randint(3, 10))
new_list = [random_list[0], random_list[2], random_list[-2]]

print("Початковий список:", random_list)
print("Новий список:", new_list)