number_of_commands = int(input())
parking_clients = {}
for _ in range(number_of_commands):
    action_list = input().split()
    if action_list[0] == "register":
        person = action_list[1]
        vehicle_number = action_list[2]
        if person in parking_clients:
            print(f'ERROR: already registered with plate number {parking_clients[person]}')
        else:
            parking_clients[person] = vehicle_number
            print(f'{person} registered {vehicle_number} successfully')
    else:
        person = action_list[1]
        if person in parking_clients:
            parking_clients.pop(person)
            print(f'{person} unregistered successfully')
        else:
            print(f'ERROR: user {person} not found')
for key, value in parking_clients.items():
    print(f'{key} => {value}')
