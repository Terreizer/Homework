import string

def get_letters(input_str):
    all_letters = string.ascii_letters

    start, end = map(all_letters.index, input_str.split('-'))

    return all_letters[start:end+1] if start <= end else all_letters[start:] + all_letters[:end+1]

print(get_letters("a-c"))
print(get_letters("a-a"))
print(get_letters("s-H"))
print(get_letters("a-A"))
