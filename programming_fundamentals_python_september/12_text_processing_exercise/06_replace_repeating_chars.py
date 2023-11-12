text = input()
final_message = ''
last_added_char = ''
for current_character in text:
    if current_character != last_added_char:
        final_message += current_character
        last_added_char = current_character
print(final_message)