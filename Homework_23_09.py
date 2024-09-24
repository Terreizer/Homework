def calculator():
    try:
        num_1 = float(input("Введіть перше число: "))
        operation = input("Введіть дію (+, -, *, /): ")
        num_2 = float(input("Введіть друге число: "))
        if operation == '+':
            result = num_1 + num_2
        elif operation == '-':
            result = num_1 - num_2
        elif operation == '*':
            result = num_1 * num_2
        elif operation == '/':
            if num_2 !=0:
                result = num_1 / num_2
            else:
                return "Помилка: ділення на нуль!"
        else:
            return "Неправильна операція!"
        return f"Результат:{result}"
    except ValueError:
        return "Помилка: введено не число!"
        print('Ошибка:', e)
print(calculator())
