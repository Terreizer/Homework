def format_time(seconds):
    if not (0 <= seconds <= 8640000):
        raise ValueError("The number must be between 0 and 8640000.")

    days, remainder = divmod(seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    if days % 10 == 1 and days % 100 != 11:
        day_word = "day"
    elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
        day_word = "day"
    else:
        day_word = "days"

    return f"{days} {day_word}, {hours:02}:{minutes:02}:{seconds:02}"

try:
    input_seconds = int(input("Enter the number of seconds (0 - 8640000): "))
    print(format_time(input_seconds))
except ValueError as e:
    print(e)
