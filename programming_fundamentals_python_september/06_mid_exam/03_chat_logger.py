command = input()
new_list = []
while command != 'end':
    current_command = command.split()[0]
    message = command.split()[1]
    if current_command == "Chat":
        new_list.append(message)
    elif current_command == 'Delete' and message in new_list:
        new_list.remove(message)
    elif current_command == 'Edit' and message in new_list:
        edited_message = command.split()[2]
        old_message_index = int(new_list.index(message))
        new_list.insert(old_message_index,edited_message)
        new_list.remove(message)
    elif current_command == 'Pin' and message in new_list:
        new_list.remove(message)
        new_list.append(message)
    elif current_command == 'Spam':
        values_to_append = command.split()
        for current_value in values_to_append:
            if current_value != current_command:
                new_list.append(current_value)
    command = input()
for item in new_list:
    print(item)