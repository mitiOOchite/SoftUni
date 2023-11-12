import string

text = input().strip().split()
current_sum = 0
for current_char in text:
    number = ''
    begining_of_string = current_char[0]
    start_number = string.ascii_letters.lower().find(begining_of_string.lower()) + 1
    end_of_string = current_char[-1]
    end_number = string.ascii_letters.lower().find(end_of_string.lower()) + 1
    current_value = 0
    for char in current_char:
        if char.isdigit():
            number += char
    if begining_of_string.isupper():
        current_value = int(number) / start_number
    else:
        current_value = int(number) * start_number
    if end_of_string.isupper():
        current_value -= end_number
    else:
        current_value += end_number
    current_sum += current_value
print(f'{current_sum:.2f}')
