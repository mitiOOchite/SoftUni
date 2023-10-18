grocery_list = input().split('!')
command = input()
while command != 'Go Shopping!':
    command_list = command.split()
    action = command_list[0]
    grocery = command_list[1]
    if action == 'Urgent' and grocery not in grocery_list:
        grocery_list.insert(0, grocery)
    elif action == "Unnecessary" and grocery in grocery_list:
        grocery_list.remove(grocery)
    elif action == "Correct" and grocery in grocery_list:
        index = grocery_list.index(grocery)
        grocery_list[index] = command_list[2]
    elif action == "Rearrange" and grocery in grocery_list:
        grocery_list.remove(grocery)
        grocery_list.append(grocery)
    command = input()

print(', '.join(grocery_list))
