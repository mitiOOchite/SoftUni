inventory = input().split(', ')
command = input()
while command != 'Craft!':
    action,item = command.split(' - ')
    if action == 'Collect' and item not in inventory:
        inventory.append(item)
    elif action == 'Drop' and item in inventory:
        inventory.remove(item)
    elif action == 'Combine Items':
        old_item,new_item = item.split(':')
        if old_item in inventory:
            old_item_index = inventory.index(old_item)
            inventory.insert(old_item_index+1,new_item)
    elif action == 'Renew' and item in inventory:
        inventory.remove(item)
        inventory.append(item)
    command = input()
print(', '.join(inventory))