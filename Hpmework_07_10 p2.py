def correct_sentence(text):
    corrected_text = '. '.join(sentence.capitalize() for sentence in text.split('. '))

    return corrected_text + '.' if not corrected_text.endswith('.') else corrected_text

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
