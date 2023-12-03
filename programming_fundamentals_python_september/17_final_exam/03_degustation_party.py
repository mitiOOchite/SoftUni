command = input()
guest_dict = {}
unliked_count = 0
while command != 'Stop':
    action, guest, food = command.split('-')
    if action == 'Like':
        if guest in guest_dict and food not in guest_dict[guest]:
            guest_dict[guest].append(food)
        elif guest not in guest_dict:
            guest_dict[guest] = [food]
    elif action == 'Dislike':
        if guest not in guest_dict:
            print(f'{guest} is not at the party.')
        elif guest in guest_dict and food in guest_dict[guest]:
            guest_dict[guest].remove(food)
            print(f"{guest} doesn't like the {food}.")
            unliked_count+= 1
        else:
            print(f"{guest} doesn't have the {food} in his/her collection.")
    command = input()
for person, food in guest_dict.items():
    print(f'{person}: {", ".join(food)}')
print(f'Unliked meals: {unliked_count}')