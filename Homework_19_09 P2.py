number = int(input("Введіть 5-ти значне число: "))
num_5 = number % 10
num_4 = (number // 10) % 10
num_3 = (number // 100) % 10
num_2 = (number // 1000) % 10
num_1 = (number // 10000)
final_number = num_5 * 10000 + num_4 * 1000 + num_3 * 100 + num_2 * 10 + num_1

print(final_number)