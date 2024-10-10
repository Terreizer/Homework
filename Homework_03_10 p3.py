def multiply_digits(n):
    product = 1
    while n > 0:
        product *= n % 10
        n //= 10
    return product

def multiply_until_single_digit(n):
    while n > 9:
        n = multiply_digits(n)
    return n

user_input = input("Введіть ціле число: ")

try:
    number = int(user_input)
    result = multiply_until_single_digit(number)
    print(result)
except ValueError:
    print("Будь ласка, введіть число.")
