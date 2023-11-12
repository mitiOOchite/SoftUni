some_string = input()
final_string = ''
strength = 0
for index in range(len(some_string)):
    # We have an explosion
    if strength > 0 and some_string[index] != '>':
        strength -= 1
    # We have an explosion symbol
    elif some_string[index] == '>':
        final_string += some_string[index]
        strength += int(some_string[index + 1])
    else:
        final_string += some_string[index]
print(final_string)