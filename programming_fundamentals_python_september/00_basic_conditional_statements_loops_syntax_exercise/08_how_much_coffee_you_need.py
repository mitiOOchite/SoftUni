current_command = input()
coffee_count = 0
total_coffee = 0
while current_command != 'END':
    if current_command.lower() == 'coding' \
            or current_command.lower() == "dog" \
            or current_command.lower() == "cat" \
            or current_command.lower() == "movie":
        if current_command.islower():
            coffee_count+= 1
        else:
            coffee_count+= 2
    current_command = input()
if coffee_count > 5:
    print('You need extra sleep')
else:
    print(coffee_count)