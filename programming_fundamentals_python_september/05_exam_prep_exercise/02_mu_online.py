def potion(max_health, heal, current_health, room_count):
    room_count += 1
    if current_health < max_health:
        if heal <= (max_health - current_health):
            current_health += heal
            print(f'You healed for {heal} hp.')
            print(f'Current health: {current_health} hp.')
        else:
            heal = max_health - current_health
            current_health += heal
            print(f'You healed for {heal} hp.')
            print(f'Current health: {current_health} hp.')
    return current_health, room_count


def attack(damage, current_health, room_count, monster):
    room_count += 1
    current_health -= damage
    if current_health <= 0:
        print(f'You died! Killed by {monster}.')
        print(f'Best room: {room_count}')
    else:
        print(f'You slayed {monster}.')
    return current_health, room_count


def add_bitcoins(bitcoins, start_bitcoins, room_count):
    start_bitcoins += bitcoins
    room_count += 1
    print(f'You found {bitcoins} bitcoins.')
    return start_bitcoins, room_count


max_health = 100
start_bitcoins = 0
rooms = input().split('|')
current_health = max_health
room_count = 0
for current_room in rooms:
    current_room_list = current_room.split()
    command = current_room_list[0]
    if command == 'potion':
        heal = int(current_room_list[1])
        current_health, room_count = potion(max_health, heal, current_health, room_count)
    elif command == 'chest':
        bitcoins = int(current_room_list[1])
        start_bitcoins, room_count = add_bitcoins(bitcoins, start_bitcoins, room_count)
    else:
        damage, monster = int(current_room_list[1]), command
        current_health, room_count = attack(damage, current_health, room_count, monster)
    if current_health <= 0:
        break
    elif room_count == len(rooms):
        print('You\'ve made it!')
        print(f'Bitcoins: {start_bitcoins}')
        print(f'Health: {current_health}')
