def calculator():
    while True:
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
                if num_2 != 0:
                    result = num_1 / num_2
                else:
                    print("Помилка: ділення на нуль!")
                    continue
            else:
                print("Неправильна операція!")
                continue

            print(f"Результат: {result}")
        except ValueError:
            print("Помилка: введено не число!")

        continue_calculation = input("Продовжити роботу калькулятора? (y/yes): ").lower()
        if continue_calculation not in ['y', 'yes']:
            print("Калькулятор завершив роботу.")
            break

calculator()
