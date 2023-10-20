dictionary = {
    "name": "Breno",
    "email": "kcnwkjcnjdsv@gmail.com",
    "phone": "(99)99999-9999"
}

print(dictionary.get('name'))
print(dictionary.get('birth_date'))
print(dictionary.get('birth_date', '01/01/1900'))


'''---------------------- Exercise --------------------------'''
number_in_words = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}
"""
cardinal_numbers = input('inseert numbers: ')

ordinal_numbers = ''

for n in cardinal_numbers:
    ordinal_numbers += f"{number_in_words.get(n)}    "

print(ordinal_numbers)"""



'''------------------------ Emoji Converter -------------------------------'''
emojis = {
    ":)": "☺️",
    ":(": "🙁"
}

message = input('> ')

splitted_message = message.split()
output = ''

for word in splitted_message:
    output += emojis.get(word, word) + ' '

print(output)
